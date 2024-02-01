#!/usr/bin/env python3

import argparse
import os
import logging
import random
import traceback
import types

# This script parses the markdown files in specified locations
# loading the Python code found in each .md file into a script that is then
# dynamically loaded into a module and used as part of the NPC generation
# process. In essence, this is a flavor of "literate programming".

SAVEPY = os.getenv('SAVE_PY')

# TODO: Refactor to use Python logging
def error(*values): logging.error(*values)
def warn(*values): logging.warn(*values)
def log(*values): logging.info(*values)
def debug(*values): logging.debug(*values)

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
        if isinstance(choices, list):
            return self.choosefromlist(choices)
        elif isinstance(choices, dict):
            return self.choosefrommap(choices)
        elif choices == None:
            return self.input("")
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

# REPOROOT is the root directory of the content; maybe at some point let this be 
# adjusted by command-line argument?
REPOROOT = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../../') + "/"

# ONLINEROOT should be the root of the repository online, via HTTP
# This should probably get picked up by environment variable or command-line arg
# at some point in the future.
ONLINEROOT = "http://worldspine.tedneward.com"

##########################
# Character-related pieces
class Feature:
    def __init__(self, title : str, text : str, recharges=None, uses=None):
        self.title = title
        self.text = text
        self.uses = uses
        self.recharges = recharges
        self.npc = None # The StatBlock to which this Feature is attached

    def markdownifytext(self):
        return self.text.replace('\n', '\n>')

    def __str__(self):
        if "{" in self.text:
            # Grab the module's __dict__ and pass it in as the globals or locals or whatever
            litexec('"f' + self.text + '"', { "self" : self })
        #if "{" in self.uses:
        #    self.uses = eval('f"' + self.uses + '"')

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
                posttitletext = f" ({self.uses}/Recharges on {self.recharges})"
        return f"***{self.title}{posttitletext}.*** {self.markdownifytext()}"

class Action(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

# This can be innate spellcasting, class-based spellcasting, or PactMagic.
# I think any sort of psionic or other abilities could fit in here as well.
# Any ability that can cast a spell as an Action is Casting as far as
# this tool is concerned.
class Casting(Action):
    def __init__(self, title):
        Action.__init__(self, title, "", recharges="long rest")

class InnateCasting(Casting):
    def __init__(self, innatetype):
        Spellcasting.__init__(self, innatetype + " Spellcasting")
        self.recharges = None
        self.perday = {}

class Spellcasting(Casting):
    def __init__(self, title, classspelllist, ability):
        Casting.__init__(self, title + " Casting")
        self.classspelllist = classspelllist
        self.ability = ability
        self.maxcantripsknown = 0
        self.cantripsknown = []
        self.slottable = {}
        self.maxspellsknown = 0
        self.spellsknown = []
        

class BonusAction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

class Reaction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

class LairAction(Feature):
    def __init__(self, title, text, uses=None, recharges=None):
        Feature.__init__(self, title, text, uses, recharges)

# Specifically for melee attack Actions; produces text like:
# "***Club.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 
# 5ft., one target. Hit: 1d4 + {STRbonus} bludgeoning damage."
class MeleeAttack(Action):
    def __init__(self, title, dmgamt, dmgtype, properties=None):
        Action.__init__(self, title, "")
        self.dmgamt = dmgamt
        self.dmgtype = dmgtype 
            # should be one of the recognized types: bludgeoning, piercing, slashing, etc
        self.properties = properties if properties != None else []
            # finesse is the only one I really care about since it changes up the ability bonus
        self.tohit = 0
        self.reach = "5ft."

    # Take finesse into account here
    def __str__(self):
        if self.npc == None: return self.title

        text  = f"***{self.title}.*** *Melee Weapon Attack:* "
        text += f"+{self.npc.STRbonus() + self.npc.proficiencybonus() + self.tohit} to hit, "
        text += f"reach {self.reach}, one target. "
        text += f"Hit: {self.dmgamt} + {self.npc.STRbonus()} {self.dmgtype}"
        return text

# Specifically for ranged attack Actions; produces text like:
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

    # TODO: Factor in ability bonus damage 
    def __str__(self):
        text  = f"***{self.title}.*** *Ranged Weapon Attack:* "
        text += f"+{self.npc.DEXbonus() + self.npc.proficiencybonus() + self.tohit} to hit, "
        text += f"range {self.range}, one target. "
        text += f"Hit: {self.dmgamt} + {self.npc.DEXbonus()} {self.dmgtype}"
        return text

class StatBlock:
    def __init__(self):
        self.name = "(Name)"
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

        self.description = []

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
        litexec("racemod.apply(self)", { "racemod" : racemod, "self": self })

    def setsubrace(self, subracemod):
        if self.subrace != None: warn("Replacing",self.subrace.name,"with",subracemod.name,"!")
        self.subrace = subracemod
        litexec("subracemod.apply(self)", { "subracemod" : subracemod, "self": self })

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

    # This is a level-up function as a side-effect
    def addclass(self, classmod):
        self.classes.append(classmod)

        def levelup(mod, level):
            everylvlfn = getattr(mod, "everylevel", None)
            if everylvlfn != None: litexec("fn(self)", { "fn" : everylvlfn, "self": self })
            levelfn = getattr(mod, "level" + str(level), None)
            if levelfn != None: litexec("fn(self)", { "fn" : levelfn, "self": self })

        # Now that we added the level, invoke the new levelX fn (if present)
        # in race, subrace (if present), class, and subclass (if present)
        totallvls = self.levels()
        levelup(self.race, totallvls)
        if self.subrace != None: levelup(self.subrace, totallvls)

        classlvls = self.levels(classmod)
        levelup(classmod, classlvls)
        if classmod.name in self.subclasses:
            subclassmod = self.subclasses[classmod.name]
            levelup(subclassmod, classlvls)

        for f in self.feats:
            childmods = getattr(moduleglobals['roots']['Feats'].childmods)
            for childmod in childmods:
                if childmod.name in self.feats:
                    levelup(childmod, totallvls)
    
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

    def applyfeat(self, featmod):
        self.feats.append(featmod.name)
        litexec("fn(self)", { "fn" : featmod.apply, "self": self })

    def addproficiency(self, proficiency):
        if proficiency in ['STR','DEX','CON','INT','WIS','CHA']:
            # It's a saving throw -- track separately in the future?
            self.proficiencies.append(proficiency)
        elif proficiency in self.proficiencies:
            self.expertises.append(proficiency)
        elif proficiency in moduleglobals['Abilities'].skills:
            # It's a skill -- track separately?
            self.proficiencies.append(proficiency)
        else:
            # It's equipment
            self.proficiencies.append(proficiency)

    def getsavingthrows(self):
        saves = []
        for p in self.proficiencies:
            if p in ['STR','DEX','CON','INT','WIS','CHA']:
                score = self.proficiencybonus() + self.abilitybonus(p)
                saves.append(f"{p} +{score}")
        return saves

    def getskills(self):
        # What about expertises?!?
        skills = []
        for p in self.expertises:
            if p not in moduleglobals['Abilities'].skills: continue
            score = (self.proficiencybonus() * 2) + self.abilitybonus(moduleglobals['Abilities'].skillability[p])
            skills.append(f"{p} +{score}")

        for p in self.proficiencies:
            if p in self.expertises: continue
            if p not in moduleglobals['Abilities'].skills: continue
            score = self.proficiencybonus() + self.abilitybonus(moduleglobals['Abilities'].skillability[p])
            skills.append(f"{p} +{score}")
        return skills

    def getproficiencies(self):
        profs = []
        for p in self.proficiencies:
            if p in ['STR','DEX','CON','INT','WIS','CHA']: continue
            if p in moduleglobals['Abilities'].skills: continue
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
    # Feature methods
    def append(self, feature : Feature):
        debug("StatBlock::append: " + feature.title)
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

    def addequipment(self, equip):
        self.equipment.append(equip)

        # Let's pull actions out for convenience
        gaa = getattr(equip, "getactions", None)
        if gaa != None:
            # This equipment has attack actions so pull 'em out
            actions = equip.getactions()
            for action in actions:
                self.append(action)

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

    # This method is the last step before an emit(), to give the StatBlock a chance
    # to organize and/or optimize itself.
    def freeze(self):
        log("StatBlock",self.name,"frozen in place.")

        # Lint the StatBlock for any warnings

        # Sort lists by alphabetical order
        self.actions.sort()
        self.bonusactions.sort()
        self.reactions.sort()
        self.lairactions.sort()
        self.equipment.sort()
        # Do NOT sort description!

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

        if len(self.equipment) > 0:
            result += ">#### Equipment\n"
            for equip in self.equipment:
                result += f">{equip}\n"
                result +=  ">\n"

        result += ">___\n"
        result += ">#### Description\n"
        for desc in self.description:
            result += f">{desc}\n"
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


def choosefromlist(self, inputlist : list):
    choicelist = []

    # If this is an actual list of string options, proceed
    if isinstance(inputlist[0], str):
        choicelist = inputlist.copy()
        choicelist.sort()
        choiceidx = 0
        for c in choicelist:
            choiceidx += 1
            self.output(f'{choiceidx}: {c}')

        # Now capture the response and determine selection
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

    # Otherwise, build out a map and choose from that
    else:
        choicemap = {}
        if getattr(inputlist[0], "name", None) != None:
            for item in inputlist:
                choicemap[item.name] = item
        elif getattr(inputlist[0], "__name__", None) != None:
            for item in inputlist:
                choicemap[item.__name__] = item
        else:
            warn("We can't figure out what to display")
            return None
        (label, choice) = self.choosefrommap(choicemap)
        return choice

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
    if isinstance(choices, list):
        return self.choosefromlist(choices)
    elif isinstance(choices, dict):
        return self.choosefrommap(choices)
    elif choices == None:
        return self.input("")
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

# A root namespace of symbols, into which modules will
# also be placed.
moduleglobals = {
    # A reference to moduleglobals itself, for breaking
    # order-dependency issues
    "roots": {},

    # Access to a few useful Python packages and builtins
    "os": os,
    #"random": random,

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

    # Utility methods of our own
    "dieroll": dieroll,
    "randomfrom": randompick,
    "randomint": randomint,
    #"randompkg": random,

    # Character-related pieces
    "Feature": Feature,
    "Action": Action,
    "Reaction": Reaction,
    "BonusAction": BonusAction,
    "LairAction": LairAction,
    "MeleeAttack": MeleeAttack,
    "RangedAttack": RangedAttack,
    "Casting": Casting,
    "InnateCasting": InnateCasting,
    "Spellcasting": Spellcasting,
}

# Take a path, and if it's a file, load a singular module.
def load(path : str, parentmodule=None, modulename=None) -> types.ModuleType:
    if os.path.isdir(path): return loaddir(path,modulename,parentmodule)
    else: return loadmodule(path,modulename,parentmodule)

# Take the given directory, look for the index.md and load that,
# then load any other files as "sub"-modules of the current one. 
def loaddir(path : str, 
            modulename : str = None, 
            parentmodule : types.ModuleType = None) -> types.ModuleType:
    if modulename == None: modulename = os.path.basename(path)

    # Look for 'index.md', load it
    module = loadmodule(path + "/index.md", modulename, parentmodule)

    # Look for other files in here and load them as modules
    # but with each one having a "parent" symbol that references
    # the index.md-based module
    setattr(module, "childmods", [])
    for f_or_d in os.listdir(path):
        if f_or_d == 'index.md': continue

        childmod = load(path + '/' + f_or_d,module,modulename + "-" + f_or_d)
        module.childmods.append(childmod)

    return module

# Take the given file (which we assume is a MD file), and
# evaluate the codeblocks inside of it as a standalone
# Python file, loading it into a module whose name is either
# derived from the filename or given in the modulename param.
def loadmodule(mdfilename : str, 
               modulename : str = None,
               parentmodule : types.ModuleType = None) -> types.ModuleType:
    global moduleglobals

    if not ismdfile(mdfilename):
        error(f"{mdfilename} is not a Markdown file!")
        return None
    
    literatecode = parsemd(mdfilename)
    if len(literatecode) > 0:
        if modulename == None:
            modulename = os.path.splitext(os.path.basename(mdfilename))[0]
        module = types.ModuleType(modulename, "Dynamically-loaded Literate Python code from " + mdfilename)
        module.__dict__.update(moduleglobals)
        exec(literatecode, module.__dict__)

        # Put parentmodule into module.parent
        if parentmodule != None:
            setattr(module, "parent", parentmodule)

        # Invoke any init function present
        init = getattr(module, "init", None)
        if init != None: module.init()

        return module
    else:
        warn(f"No literate Python found in {mdfilename}")
        return None

# Load a directory as a "root" module, which means we auto-export
# (to moduleglobals) some symbols from the top-level module for 
# convenience, as well as capture the module itself in the top-level
def loadroot(path : str) -> types.ModuleType:
    global moduleglobals
    log("Loading root " + path)

    rootmod = load(path)
    moduleglobals[rootmod.name] = rootmod
    moduleglobals['roots'][rootmod.name] = rootmod

    # Now pull exports out too
    if getattr(rootmod, "exports", None) != None:
        for item in rootmod.exports:
            if getattr(rootmod, item.__name__, None) != None:
                if item.__name__ in moduleglobals.keys():
                    warn(item.__name__ + " is about to be overwritten!")
                moduleglobals[item.__name__] = item

    log("Root module " + rootmod.name + " loaded")

# Go through all the root modules, and refactor their module.__dict__
# to reflect all of what's in moduleglobals?
def fixuproots() -> None:
    def fixup(module) -> None:
        #log("Fixing up " + str(module.__name__))
        module.__dict__.update(moduleglobals)
        childmods = getattr(module, "childmods", None)
        if childmods != None:
            for childmod in childmods:
                fixup(childmod)

    # Backport all the rootmodules to other rootmodules
    for rootmodname in moduleglobals['roots']:
        rootmod = moduleglobals['roots'][rootmodname]
        fixup(rootmod)

def litexec(source : str, litlocals : dict[str, object]) -> None:
    #debug("============ Executing lit Python with moduleglobals = " + dumpfirstlevel(moduleglobals))
    exec(source, moduleglobals, litlocals)
    

##########################
# Main entrypoint and workhorse
def generate(randomlist=[]):
    global shell

    npc = StatBlock()

    # Generate the random bits
    oldio = shell.io
    shell.io = RandomInput()

    abilities = False
    background = False
    gender = False
    race = False

    classgen = [] # The classes to generate randomly
    for r in randomlist:
        if r.find("Class-") > -1:
            # We're going to generate some class levels
            classgen.append(r)
        elif r == 'Abilities':
            litexec("Abilities.random(npc)", { "npc" : npc })
            abilities = True
        elif r == 'Background':
            #litexec("Background.random(npc)", { "npc" : npc })
            background = True
        elif r == 'Gender': 
            npc.gender = randompick(['Male', 'Female'])
            gender = True
        elif r == 'Race':
            litexec("Races.random(npc)", { "npc" : npc })
            race = True
        else:
            error("Unrecognized root:" + r)

    reqs = ['Abilities', 'Background', 'Gender', 'Race']
    if abilities: reqs.remove('Abilities')
    if background: reqs.remove('Background')
    if gender: reqs.remove('Gender')
    if race: reqs.remove('Race')

    shell.io = oldio
    while len(reqs) > 0:
        which = shell.choosefromlist(reqs)
        if which == 'Abilities':
            (_, abilityfn) = shell.choosefrommap(moduleglobals['roots']['Abilities'].methods)
            scores = abilityfn()
            print("Scores: ", scores)
            npc.addabilities(scores)
        elif which == 'Background':
            print("Background!")
        elif which == 'Gender':
            npc.gender = shell.choosefromlist(['Male', 'Female'])
        elif which == 'Race':
            racemod = shell.choosefromlist(moduleglobals['roots']['Races'].childmods)
            npc.setrace(racemod)
            if getattr(racemod, "childmods", None) != None:
                if len(racemod.childmods) > 0:
                    subracemod = shell.choosefromlist(racemod.childmods)
                    npc.setsubrace(subracemod)
        reqs.remove(which)

    # Now randomize some class levels
    shell.io = RandomInput()
    for cg in classgen:
        # We expect Class to look like one of a few flavors:
        # "Class": random number of levels in a random class/subclass
        # "Class-(classname)": random number of levels in classname/random-subclass
        # "Class-(classname)-(level)": level number of levels in classname/random-subclass
        parts = cg.split('-')
        if len(parts) == 1:
            print("Random number of levels in a random class/subclass")
        elif len(parts) == 2:
            print("Random number of levels in class/subclass", parts[1])
        elif len(parts) == 3:
            print(parts[2],"levels in",parts[1])
            for _ in range(0, int(parts[2])):
                classmod = moduleglobals['roots']['Classes'].childmods[parts[1]]
                npc.addclass(classmod)

    # Now interactively gen some class levels
    shell.io = oldio

    choice = shell.choose("Add a new level? ", ['Yes', 'No'])
    while (choice == 'Yes'):
        print(rootdict['Classes'].modules)
        (_, classmod) = shell.choosefrommap(rootdict['Classes'].modules)
        npc.addclass(classmod)
        npc.levelup(npc.levels(classmod))

    return npc

def main():
    global shell
    global SAVEPY

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs using PC rules/templates'
	)
    parser.add_argument('--verbosity', choices=['quiet', 'verbose'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--savepy', help="Which modules to save literate-parsed Python code (into ./Python)")
    parser.add_argument('--scripts', nargs='*', help="A list of files to use as scripted input")
    parser.add_argument('--randomize', help="List of things to generate randomly ahead of time (interactive only)")
    parser.add_argument("--nop", help="Do nothing after loading; this is to test the module-loading initialization")
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbosity != None:
        if args.verbosity == 'verbose':
            logging.basicConfig(level = logging.DEBUG)
        elif args.verbosity == 'quiet':
            logging.basicConfig(level = logging.WARNING)
    else:
        print("Running non-verbose")
        logging.basicConfig(level = logging.INFO)

    # Save the loaded literate Python somewhere (for easier debugging)?
    if args.savepy != None:
        SAVEPY = args.savepy
    
    # Load modules, have them bootstrap in turn
    loadroot(REPOROOT + "Abilities")
    loadroot(REPOROOT + "Races")
    #loadrootmodule(REPOROOT + "Backgrounds")
    loadroot(REPOROOT + "Classes")
    loadroot(REPOROOT + "Equipment")
    loadroot(REPOROOT + "Feats")
    #loadrootmodule(REPOROOT + "Creatures") # <-- this will be an interesting day
    fixuproots()


    if args.nop != None: return

    # Examine command line, let's see if we need to script-generate
    # our PC/NPC, or if we do it interactively.
    if args.scripts != None:
        for script in args.scripts:
            shell.io = ScriptedInput(script)
            npc = generate()
            # Write to "{script}.md" file
            print(npc.emitmd())
    else:
        print("Randomly generating a character's",args.randomize)
        shell.io = TerminalInput()
        npc = None
        if args.randomize != None:
            npc = generate(args.randomize.split(','))
        else:
            npc = generate()
        # Write to "output.md"
        print(npc.emitmd())

if __name__ == '__main__':
	main()
