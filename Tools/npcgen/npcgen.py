#!/usr/bin/env python3

import argparse
import os
import random
import traceback
import types

# This script parses the markdown files in specified locations
# loading the Python code found in each .md file into a script that is then
# dynamically loaded into a module and used as part of the NPC generation
# process. In essence, this is a flavor of "literate programming".

quiet = False
verbose = False
SAVEPY = os.getenv('SAVE_PY')

def error(*values):
    print(*values)

def warn(*values):
    if not quiet:
        print("WARNING: ", end='')
        print(*values)

def log(*values):
    if verbose and not quiet:
        print(*values)

# TODO: REPOROOT should be picked up from an environment variable, or a default
# file location (like a .properties file equivalent). If not, default to a location-
# based approach from this location.
REPOROOT = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../../') + "/"

# ONLINEROOT should be the root of the repository online, via HTTP
ONLINEROOT = "http://worldspine.tedneward.com"

##########################
# Character-related pieces
class Feature:
    def __init__(self, title, text, recharges=None, uses=None):
        self.title = title
        self.text = text
        self.uses = uses
        self.recharges = recharges
        self.npc = None # The StatBlock to which this Feature is attached

    def __str__(self):
        posttitletext = ""
        if self.recharges == None:
            if self.uses == None:
                # At-will
                posttitletext = ""
            else:
                # It's a 2/day but never recharges?
                # Pretty sure this isn't a thing
                warn(self.title, "has uses but no recharges text!")
                posttitletext = f"({self.uses})"
        else:
            if self.recharges == "short rest": self.recharges = "short or long rest"

            if self.uses == None:
                posttitletext = f" (Recharges on {self.recharges})"
            else:
                posttitletext = " ({self.uses}/Recharges on {self.recharges})"
        return f"***{self.title}{posttitletext}.*** {self.text}"

class Action(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

class BonusAction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

class Reaction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

class LairAction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

# Specifically for melee attack Actions; produces text similar to:
# "***Club.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 
# 5ft., one target. Hit: 1d4 + {STRbonus} bludgeoning damage."
class MeleeAttack(Action):
    def __init__(self, title, dmgamt, dmgtype, properties=None):
        Action.__init__(self, title, "")
        self.dmgamt = dmgamt
        self.dmgtype = dmgtype 
            # should be one of the recognized types: bludgeoning, piercing, slashing, etc
        self.properties = properties if properties != None else []
            # light, finesse, two-handed, versatile, etc
        self.tohit = 0
        self.reach = "5ft."

    def __str__(self):
        text  = f"***{self.title}.*** *Melee Weapon Attack:* "
        text += f"+{self.npc.STRbonus() + self.npc.proficiencybonus() + self.tohit} to hit, "
        text += f"range {self.reach}, one target. "
        text += f"Hit: {self.dmgamt} {self.dmgtype}"
        return text

# Specifically for ranged attack Actions; produces text similar to:
# "***Shortbow.*** *Ranged Weapon Attack:* +{proficiency bonus + DEXbonus} to hit, 
# range 80/200, one target. Hit: 1d4 + {STRbonus} bludgeoning damage."
class RangedAttack(Action):
    def __init__(self, title, range, dmgamt, dmgtype, properties=None):
        Action.__init__(self, title, "")
        self.tohit = 0
        self.range = range
        self.dmgamt = dmgamt
        self.dmgtype = dmgtype 
            # should be one of the recognized types: bludgeoning, piercing, slashing, etc
        self.properties = properties if properties != None else []
            # thrown, ammunition, etc

    def __str__(self):
        text  = f"***{self.title}.*** *Ranged Weapon Attack:* "
        text += f"+{self.npc.DEXbonus() + self.npc.proficiencybonus() + self.tohit} to hit, "
        text += f"range {self.range}, one target. "
        text += f"Hit: {self.dmgamt} {self.dmgtype}"
        return text

class StatBlock:
    def __init__(self):
        self.name = ""
        self.size = 'Medium'
        self.type = ''
        self.gender = ''

        self.race = None        # module reference
        self.subrace = None     # optional module reference
        self.classes = []       # list of module references
        self.subclasses = {}    # dict of classmodule.name : subclass module references

        self.hitpoints = 0      # running total of HP
        self.hitdice = { 'd6':0, 'd8':0, 'd10':0, 'd12':0, 'd20':0 }
        self.hpconbonus = 0     # running total of CON bonuses

        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0

        self.profbonus = 0

        self.speed = { 'walking': 0 }
        self.senses = { 'passive Perception': 0 }
        self.armorclass = { }
        self.damagevulnerabilities = []
        self.damageresistances = []
        self.damageimmunities = []
        self.conditionimmunities = []

        # Proficiencies are skills, weapons, armors, and saving throws
        # Expertises are double-counted proficiencies (add proficiency bonus twice)
        self.proficiencies = []
        self.expertises = []
        self.languages = [] # These are kinda proficiencies, but displayed separately, so....

        self.traits = []
        self.actions = []
        self.bonusactions = []
        self.reactions = []
        self.lairactions = []

        self.feats = []

        self.equipment = []

    ##########################
    # Ability-related methods
    def getability(self, name): return getattr(self, name, 0)
    def setability(self, name, score): setattr(self, name, score)
    def addabilities(self, abilities):
        for name in abilities:
            self.setability(name, abilities[name] + self.getability(name))

    def STRbonus(self): return (self.STR // 2) - 5
    def DEXbonus(self): return (self.DEX // 2) - 5
    def CONbonus(self): return (self.CON // 2) - 5
    def INTbonus(self): return (self.INT // 2) - 5
    def WISbonus(self): return (self.WIS // 2) - 5
    def CHAbonus(self): return (self.CHA // 2) - 5
    def abilitybonus(self, name):
        if name == 'STR': return self.STRbonus()
        elif name == 'DEX': return self.DEXbonus()
        elif name == 'CON': return self.CONbonus()
        elif name == 'INT': return self.INTbonus()
        elif name == 'WIS': return self.WISbonus()
        elif name == 'CHA': return self.CHAbonus()
        else:
            error("Unrecognized ability bonus request:", name)
            return None

    ##########################
    # Race-related methods
    def setrace(self, racemod):
        if self.race != None: warn("Replacing",self.race.name,"with",racemod.name,"!")
        self.race = racemod
        racemod.apply(self)

    def setsubrace(self, subracemod):
        if self.subrace != None: warn("Replacing",self.subrace.name,"with",subracemod.name,"!")
        self.subrace = subracemod
        subracemod.apply(self)

    ##########################
    # Class-related methods

    def hits(self, die):
        self.hitdice[die] += 1
        if self.levels() == 1:
            # Max hit points at first level
            self.hitpoints += int(die[1:]) # Strip off the 'd'
        else:
            # We roll randomly (sort of)
            top = int(die[1:])
            self.hitpoints += random.randrange(4, top)
        # Keep a running total for the CON bonus, since it can change over time/levels
        self.hpconbonus += self.CONbonus()
        # Likewise, keep a running total for hit points
        self.hitpoints += self.CONbonus()

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)

    # Revisit this when we get to monsters-having-classes
    # since technically monsters have no levels, so should their
    # PB add to their class levels?!?
    def proficiencybonus(self):
        if self.profbonus == 0:
            return (self.levels() // 4) + 2
        else:
            return self.profbonus

    def levels(self, clss = None):
        if clss == None: return len(self.classes)
        else:
            count = 0
            if isinstance(clss, str):
                for cli in self.classes:
                    if cli.name == clss: count += 1
            else:
                for cli in self.classes: 
                    if cli == clss: count += 1
            return count

    def applyfeat(self, featname, featmod):
        self.feats.append(featname)
        featmod.apply(self)

    def getsavingthrows(self):
        saves = []
        for p in self.proficiencies:
            if p in ['STR','DEX','CON','INT','WIS','CHA']:
                score = self.proficiencybonus() + self.abilitybonus(p)
                saves.append(f"{p} +{score}")
        return saves

    def getskills(self):
        skills = []
        for p in self.proficiencies:
            if p not in roots['Abilities'].skills: continue
            score = self.proficiencybonus() + self.abilitybonus(roots['Abilities'].skillability[p])
            skills.append(f"{p} +{score}")
        return skills

    def getproficiencies(self):
        profs = []
        for p in self.proficiencies:
            if p in ['STR','DEX','CON','INT','WIS','CHA']: continue
            if p in roots['Abilities'].skills: continue
            profs.append(p)
        return profs
    
    def getlanguages(self): return self.languages

    def getsenses(self):
        items = []
        for (key, value) in self.senses.items():
            if key == 'passive Perception':
                if 'Perception' in self.expertises:
                    items.append(f"passive Perception {10 + value + self.WISbonus() + (self.proficiencybonus() * 2)}")
                elif 'Perception' in self.proficiencies:
                    items.append(f"passive Perception {10 + value + self.WISbonus() + self.proficiencybonus()}")
                else:
                    items.append(f"passive Perception {10 + value + self.WISbonus()}")
            else:
                items.insert(0, f"{key} {value}")
        return items

    ##########################
    # "Deference": some abilities/scores/etc need to be calculated not
    # at the time they are added, but 


    ##########################
    # Feature methods
    def append(self, feature : Feature):
        log("StatBlock::append",feature.title)
        if isinstance(feature, MeleeAttack): self.actions.append(feature)
        elif isinstance(feature, RangedAttack): self.actions.append(feature)
        elif isinstance(feature, Action): self.actions.append(feature)
        elif isinstance(feature, BonusAction): self.bonusactions.append(feature)
        elif isinstance(feature, Reaction): self.reactions.append(feature)
        elif isinstance(feature, LairAction): self.lairactions.append(feature)
        else: self.traits.append(feature)
        feature.npc = self

    def find(self, featuretitle : str) -> Feature|None:
        for f in self.traits | self.actions | self.bonusactions | self.reactions | self.lairactions:
            if f.title == featuretitle:
                return f
        return None
    
    def findall(self, featuretitle : str) -> list:
        results = []
        for f in self.traits | self.actions | self.bonusactions | self.reactions | self.lairactions:
            if featuretitle in f.title:
                results.append(f)
        return results
    
    def replace(self, feature : Feature) -> bool:
        def replacebytype(srclist, feature):
            for f in srclist:
                if f.title == feature.title:
                    srclist.remove(f)
                    srclist.append(feature)
                    feature.npc = self
                    return True
            return False

        if isinstance(feature, Action) and replacebytype(self.actions, feature): return True
        if isinstance(feature, BonusAction) and replacebytype(self.bonusactions, feature): return True
        if isinstance(feature, Reaction) and replacebytype(self.reactions, feature): return True
        if isinstance(feature, LairAction) and replacebytype(self.lairactions, feature): return True

        for f in self.traits:
            if f.title == feature.title:
                self.traits.remove(f)
                self.traits.append(feature)
                feature.npc = self
                return True

        return False

    ##########################
    # Emitter methods
    def getracesubstring(self):
        return f"{self.race.type} ({'' if self.subrace == None else self.subrace.name + ' '}{self.race.name})"
    
    def getclasssubstring(self):
        if self.levels() < 1: return ""

        classmap = {}
        for c in self.classes:
            if c not in classmap:
                classmap[c] = 1
            else:
                classmap[c] += 1

        strs = []
        for c in classmap:
            if c in self.subclasses.keys():
                strs.append(f"{c.name} ({self.subclasses[c].name}) {classmap[c]}")
            else:
                strs.append(f"{c.name} {classmap[c]}")
        return "/".join(strs)

    def emitmd(self) -> str:
        linesep = ">___\n"

        result = ""

        def emitheaderblock():
            text =  f">### {self.name}\n"
            text += f'>*{self.size} {self.gender} {self.getracesubstring()} {self.getclasssubstring()}, any alignment*\n'
            text += linesep
            return text
        
        def emitsecondaryheaderblock():
            def getarmorclass():
                result = []
                ac = 10
                for (actext, acnum) in self.armorclass.items():
                    if acnum > 8:
                        # Only armor itself is ever a value 10+
                        ac = acnum
                        result.append(f'{actext} ({acnum})')
                    else:
                        ac += acnum
                        result.append(f'{actext} (+{acnum})')
                if self.DEXbonus() != 0:
                    ac += self.DEXbonus()
                    result.append(f'DEX ({self.DEXbonus():+g})')
                return str(ac) + ' (' + ",".join(result) + ')'
            
            def getspeed():
                text = str(self.speed['walking']) + ' ft'
                for (key, value) in self.speed.items():
                    if key == 'walking': continue
                    else:
                        text += ", " + key + " " + str(value) + " ft"
                return text

            text  = f">- **Armor Class** {getarmorclass()}\n"
            text += f">- **Hit Points** {self.hitpoints} ({self.hitdicedesc()} + {self.hpconbonus})\n"
            text += f">- **Speed** {getspeed()}\n"
            text += linesep
            return text

        def emitabilityblock():
            text  =  ">|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|\n"
            text +=  ">|:-:|:-:|:-:|:-:|:-:|:-:|\n"
            text += f">|{self.STR} ({self.STRbonus():+g})"
            text += f"|{self.DEX} ({self.DEXbonus():+g})"
            text += f"|{self.CON} ({self.CONbonus():+g})"
            text += f"|{self.INT} ({self.INTbonus():+g})"
            text += f"|{self.WIS} ({self.WISbonus():+g})"
            text += f"|{self.CHA} ({self.CHAbonus():+g})|\n"
            text += linesep
            return text
        
        def emitproficienciesblock():
            text  = f">- **Proficiency Bonus** {self.proficiencybonus():+g}\n"
            text += f">- **Saving Throws** {','.join(self.getsavingthrows())}\n"
            text += f">- **Damage Vulnerabilities** {','.join(self.damagevulnerabilities)}\n"
            text += f">- **Damage Resistances** {','.join(self.damageresistances)}\n"
            text += f">- **Damage Immunities** {','.join(self.damageimmunities)}\n"
            text += f">- **Condition Immunities** {','.join(self.conditionimmunities)}\n"
            text += f">- **Skills** {','.join(self.getskills())}\n"
            text += f">- **Proficiencies** {','.join(self.getproficiencies())}\n"
            text += f">- **Senses** {','.join(self.getsenses())}\n"
            text += f">- **Languages** {','.join(self.languages)}\n"
            text += linesep
            return text

        result += emitheaderblock()
        result += emitsecondaryheaderblock()
        result += emitabilityblock()
        result += emitproficienciesblock()

        if len(self.traits):
            for trait in self.traits:
                result += f">{trait}\n"
                result +=  ">\n"

        if len(self.actions):
            result +=  ">#### Actions\n"
            for action in self.actions:
                result += f">{action}\n"
                result +=  ">\n"

        if len(self.bonusactions):
            result +=  ">#### Bonus Actions\n"
            for action in self.bonusactions:
                result += f">{action}\n"
                result +=  ">\n"

        if len(self.reactions):
            result +=  ">#### Reactions\n"
            for action in self.reactions:
                result += f">{action}\n"
                result +=  ">\n"

        if len(self.lairactions):
            result +=  ">#### Lair Actions\n"
            for action in self.lairactions:
                result += f">{action}\n"
                result +=  ">\n"

        return result

##########################
# Some utility methods for use within the literate modules
def dieroll(dpattern : str) -> int:
    adj = 0
    if dpattern.find("+") > -1:
        adjustmentstr = dpattern.split("+")[1]
        adj = int(adjustmentstr)
        dpattern = dpattern.split("+")[0]
    elif dpattern.find("-") > -1:
        adjustmentstr = dpattern.split("-")[1]
        adj = - int(adjustmentstr)
        dpattern = dpattern.split("-")[0]

    (number, size) = dpattern.split("d")
    if number == '': number = 1
    accum = 0
    for _ in range(int(number)):
        accum += random.randint(1, int(size))
    return accum + adj

def randomint(start : int, end : int) -> int:
    return random.randint(start, end)

def randompick(src):
    if isinstance(src, list):
        return src[random.randint(0, len(src)-1)]
    elif isinstance(src, dict):
        key = list(src.keys())[random.randint(0, len(src)-1)]
        return (key, src[key])
    else:
        error("What the heck is src here?", src)
        return None

def creaturelinkify(name):
    linkdest = name.lower().replace(' ','-').replace("'","")
    return f"[{name}]({ONLINEROOT}/creatures/{linkdest}/)"

def itemlinkify(name):
    linkdest = name.lower().replace(' ','-').replace("'","")
    return f"[{name}]({ONLINEROOT}/magic/items/{linkdest}/)"

def spelllinkify(name):
    linkdest = name.lower().replace(' ','-').replace("'","")
    return f"[{name}]({ONLINEROOT}/magic/spells/{linkdest}/)"


##########################
# I/O infrastructure

class Input:
    def output(self, *values):
        # NOP; Expected to be overridden in derived classes
        pass

    def input(self, prompt : str = "") -> str:
        # NOP; Expected to be overridden in derived classes
        pass

    def choosefromlist(self, choicelist : list):
        choicelist.sort()
        choiceidx = 0
        for c in choicelist:
            choiceidx += 1
            self.output(f'{choiceidx}: {c}')

        response = None
        while response == None:
            response = self.input()
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choicelist):
                response = None

        response = int(response) - 1 # Account for z'ero-based 'index
        self.output("You chose " + choicelist[response])
        return choicelist[response]

    def choosefrommap(self, choicemap):
        keys = list(choicemap.keys())
        keys.sort()
        choiceidx = 0
        for k in keys:
            choiceidx += 1
            c = choicemap[k]
            self.output(f'{choiceidx}: {k} ({c})')

        # Interactive
        response = None
        while response == None:
            response = self.input()
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choicemap):
                response = None

        responseidx = int(response) - 1 # Account for z'ero-based 'index
        responsekey = keys[responseidx]
        self.output("You chose " + str((responsekey, choicemap[responsekey])))
        return (responsekey, choicemap[responsekey])

    def choose(self, prompt, choices=None):
        self.output(prompt)
        if choices == None:
            return self.input("")
        elif isinstance(choices, list):
            return self.choosefromlist(choices)
        elif isinstance(choices, dict):
            return self.choosefrommap(choices)
        else:
            error("WTF?!?", choices)

class TerminalInput(Input):
    def output(self, *values): print(*values)

    def input(self, prompt : str = "") -> str: return input(prompt + " >>> ")

class ScriptedInput(Input):
    def __init__(self, inputfile):
        self.inputfile = inputfile
        self.answers = []

        # TODO Parse inputfile, load answers, capture them.
        # Then we can feed each one as input until we run out.

    def output(self, *values): print(*values)

    def input(self, prompt : str = "") -> str: return input(prompt + ">>> ")

class RandomInput(Input):
    def output(self, *values): print(*values)

    def choosefromlist(self, choicelist : list):
        response = random.randint(0, len(choicelist)-1)
        self.output("I chose " + choicelist[response])
        return choicelist[response]

    def choosefrommap(self, choicemap):
        keys = list(choicemap.keys())
        responseidx = random.randint(0, len(keys)-1)
        responsekey = keys[responseidx]
        self.output("I chose " + str((responsekey, choicemap[responsekey])))
        return (responsekey, choicemap[responsekey])

# We need a constant object in place since this gets passed into each of the loaded
# modules to use as an I/O facility; so we "wrap" the Input object, thus allowing us
# to replace it without anyone being the wiser.
class Shell:
    def __init__(self, io):
        self.io = io

    def input(self, prompt : str = "") -> str: return self.io.input(prompt)

    def output(self, *values): return self.io.output(*values)

    def choosefromlist(self, choicelist : list): return self.io.choosefromlist(choicelist)

    def choosefrommap(self, choicemap): return self.io.choosefrommap(choicemap)

    def choose(self, prompt, choices=None): return self.io.choose(prompt, choices)

shell = Shell(TerminalInput())

##########################
# Module infrastructure

def ismdfile(filepath : str) -> bool:
    return os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.md'

def parsemd(mdfilename : str) -> str:
    pythoncode = ""
    if not ismdfile(mdfilename): error(f"{mdfilename} is not a Markdown file!")
    with open(mdfilename) as mdfile:
        lines = mdfile.readlines()
        codeblock = False
        for line in lines:
            if line[0:3] == "```":
                codeblock = not codeblock
                continue

            if codeblock == True:
                pythoncode += line

    if SAVEPY != None and SAVEPY in mdfilename:
        with open('./Python/' + os.path.basename(mdfilename) + '.py', 'w') as pyfile:
            pyfile.write(pythoncode)

    return pythoncode

# The "root" is a root namespace for any loaded modules, such as
# classes, races, backgrounds, etc. Key will be the lowercased
# directory name that loaded the "root" module,
# so all Races (and the module Races/index.md) will be "races"
# and all Classes (Classes/index.md) will be "classes".
roots = {}

def listdirwithoutdeps(path, dependencies=[]):
    retlist = []
    for it in os.listdir(path):
        if it not in dependencies:
            retlist.append(it)
    return retlist

# Root modules are Races, Classes, Equipment, Backgrounds, Feats, and other
# top-level directories in the Worldspine directory structure.
#
# A root module will contain a few things, typically:
# * submodules: the dict of Xs (races, classes, etc) that make up the collection
#    of options available to be selected; the key is a string containing the
#    submodule's human-friendly name and the value is the module loaded.
#    Each of these submodules may have "subXs" (races-subraces, classes-subclasses),
#    which makes naming variables for all this stuff really tricky.
# * random: a function designed to select a random (whatever), along with all
#    possible additional selectable options, for this root module.
def loadrootmodule(dirname : str) -> types.ModuleType:
    global roots

    if not os.path.isdir(dirname):
        error(f"{dirname} is not a root module")
        return None
    
    # Look for an index.md, loadmodule() it, apply() it,
    # then go after dependentmodules, 
    # then load submodules
    rootmodname = os.path.splitext(os.path.basename(dirname))[0]
    rootmod = loadmodule(dirname + "/index.md", rootmodname)

    roots[rootmodname] = rootmod

    # This is a root module, so it's always going to have submodules
    # So let's define a top-level dictionary in the rootmod to hold
    # those submodules; within the rootmod, we call it "modules"
    # because otherwise we have submodules, subsubmodules, 
    # and subsubsubmodules and it just gets worse from there...
    setattr(rootmod, "modules", {})
    modules = getattr(rootmod, "modules", None)

    rootmoddeps = getattr(rootmod, "dependencies", [])
    rootmoddeps.append('index.md')

    # Now look in the directory itself and loadmodule() each
    # md file in the directory (except index.md) and leave out
    # any file marked as a dependency.
    for entry in listdirwithoutdeps(dirname, rootmoddeps):
        # If the entry is a directory, then there's sub-submodules
        # and we want to load the whole mess
        if os.path.isdir(dirname + "/" + entry):
            moduleplural = "sub" + rootmodname.lower()

            entrydirname = dirname + "/" + entry

            # First load the index.md in that directory
            mod = loadmodule(entrydirname + "/index.md", (rootmodname + "-" + entry), rootmod)
            modname = getattr(mod, "name", None)
            if modname == None:
                error("Module",dirname + "/" + entry,"must have a name!")
            modules[modname] = mod
            # Set up sub-(whatevers) in the mod
            setattr(mod, moduleplural, {})

            # If that mod has a "dependencies", then make sure we don't load them
            # as subs of that entry
            dependencies = getattr(mod, "dependencies", [])
            dependencies.append('index.md')

            # Then load the other files as subs of the entry
            for entrymd in listdirwithoutdeps(dirname + "/" + entry, dependencies):
                entrymdname = dirname + "/" + entry + "/" + entrymd

                entrymod = loadmodule(entrymdname, (rootmodname + "-" + entry + "-" + entrymd)[:-3], mod)
                subs = getattr(mod, moduleplural, None)
                subs[entrymod.name] = entrymod

        # Otherwise it's just a standalone .md file, so just load that singly.
        else:
            submodname = (rootmodname + "-" + entry)[:-3]
            submodmod = loadmodule(dirname + '/' + entry, submodname, rootmod)
            submodhumanname = getattr(submodmod, "name", None)
            modules[submodhumanname] = submodmod
    return rootmod

def loadmodule(filename : str, modulename : str = None, parent : types.ModuleType = None) -> types.ModuleType:
    def enhance(module):
        global roots
        global io

        mybuiltins = {
            # Access to a few useful Python packages and builtins
            "os": os,
            #"random": random,
            "int": int,
            "str": str,

            # Our roots-level modules
            "roots": roots,

            # Our I/O facilities
            "log": log,
            "warn": warn,
            "error": error,
            "print": shell.output,
            "choose": shell.choose,

            # Some helper methods
            "creaturelink": creaturelinkify,
            "itemlink": itemlinkify,
            "spelllink": spelllinkify,

            # Module facilities
            "parent": parent,

            # Utility methods of our own
            "dieroll": dieroll,
            "randomfrom": randompick,
            "randomint": randomint,
            "randompkg": random,

            # Character-related pieces
            "Feature": Feature,
            "Action": Action,
            "Reaction": Reaction,
            "BonusAction": BonusAction,
            "LairAction": LairAction,
            "MeleeAttack": MeleeAttack,
            "RangedAttack": RangedAttack,
        }
        for (key, value) in mybuiltins.items():
            module.__dict__[key] = value

    if not quiet: log(f"Loading module found in {filename}")
    literatecode = parsemd(filename)
    if len(literatecode) > 0:
        #log(f"Literate code, {filename}:", literatecode)
        if modulename == None:
            modulename = os.path.splitext(os.path.basename(filename))[0]
        module = types.ModuleType(modulename)
        log(f"Loaded {modulename}")
        enhance(module)
        exec(literatecode, module.__dict__)

        # Lets clean up the module.__dict__ of stuff
        # that Python puts there by default, since I really
        # don't think we'll ever need it.
        del module.__dict__['__builtins__']

        # If the module defines an "init" method, invoke it
        if getattr(module, "init", None) != None:
            module.init()

        # If the module defines a "dependencies" list,
        # iterate and loadmodule() each of those in turn
        if getattr(module, "dependencies", None) != None:
            # Iterate and invoke
            for dep in module.dependencies:
                depfilename = os.path.dirname(filename) + "/" + dep
                depmodule = loadmodule(depfilename, modulename + "-" + dep, module)
                if getattr(depmodule, "init", None) != None:
                    depmodule.init()
        
        return module
    else:
        warn(f"{filename} has no literate code")
        return None



##########################
# Main entrypoint and workhorse
def generate(randomlist=[]):
    global shell
    global roots

    npc = StatBlock()

    # We need to do a few things before we can start kicking off levels,
    # but we might want to do them in a variety of different orders
    reqs = ['Abilities', 'Background', 'Gender', 'Race',] #'Class'

    oldio = shell.io
    shell.io = RandomInput()
    for r in randomlist:
        if r == 'Abilities':
            roots['Abilities'].random(npc)
        elif r == 'Background':
            #randompick(roots["Backgrounds"]).random(npc)
            shell.output("Background!")
        elif r == 'Class':
            shell.output("Classes!")
        elif r == 'Gender': 
            npc.gender = randompick(['Male', 'Female'])
        elif r == 'Race':
            roots["Races"].random(npc)
        else:
            shell.output(r + ":", roots[r].random())
        reqs.remove(r)

    shell.io = oldio
    while len(reqs) > 0:
        which = shell.choosefromlist(reqs)
        if which == 'Abilities':
            print(roots['Abilities'].random())
        elif which == 'Background':
            print("Background!")
        elif which == 'Gender':
            print(shell.choosefromlist(['Male', 'Female']))
        elif which == 'Race':
            (_, racemod) = shell.choose(roots['Races'].modules)
            if getattr(racemod, "subraces", None) != None:
                (_, subracemod) = shell.choose(racemod.subraces)
                print(f"Race: {subracemod.name} {racemod.name}")
            else:
                print(f"Race: {racemod.name}")
        reqs.remove(which)

    return npc

def main():
    global verbose
    global quiet
    global io
    global SAVEPY

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs using PC rules/templates'
	)
    parser.add_argument('--verbosity', choices=['quiet', 'verbose'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--savepy', help="Which modules to save literate-parsed Python code (into ./Python)")
    parser.add_argument('--scripts', nargs='*', help="A list of files to use as scripted input")
    parser.add_argument('--randomize', help="List of things to generate randomly ahead of time (interactive only)")
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbosity != None:
        if args.verbosity == 'verbose':
            verbose = True
        elif args.verbosity == 'quiet':
            quiet = True

    # Save the loaded literate Python somewhere (for easier debugging)?
    if args.savepy != None:
        SAVEPY = args.savepy
    
    # Load modules, have them bootstrap in turn
    loadrootmodule(REPOROOT + "Abilities")
    #loadrootmodule(REPOROOT + "Backgrounds")
    #loadrootmodule(REPOROOT + "Classes")
    loadrootmodule(REPOROOT + "Equipment")
    loadrootmodule(REPOROOT + "Feats")
    loadrootmodule(REPOROOT + "Races")
    #loadrootmodule(REPOROOT + "Creatures") # <-- this will be an interesting day

    # Test zone
    def testzone():
        #print(roots['Races'].random())
        #print(roots['Equipment'].weapons)
        #print(roots['Equipment'].armor)
        #print(roots['Feats'].choosefeat())
        #print(roots['Abilities'].abilityscoreincrease())

        npc = StatBlock()
        npc.name = "Fred Flintstone"
        npc.gender = 'Male'
        npc.addabilities(roots['Abilities'].average())
        npc.setrace(roots['Races'].modules['Half-Orc'])
        npc.proficiencies.append('STR')
        npc.proficiencies.append('CON')
        npc.append(roots['Equipment'].weapons['simple-melee']['Club'])
        print(npc.emitmd())

    # Examine command line, let's see if we need to script-generate
    # our PC/NPC, or if we do it interactively.
    if args.scripts != None:
        for script in args.scripts:
            if script == 'Test':
                testzone()
            else:
                shell.io = ScriptedInput(script)
                npc = generate()
                print(npc.emitmd())
    else:
        print("Randomly generating a character's",args.randomize)
        npc = generate(args.randomize.split(','))
        print(npc.emitmd())

if __name__ == '__main__':
	main()
