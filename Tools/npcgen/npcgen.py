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

##########################
# Character-related pieces
class Feature:
    def __init__(self, title, text, uses=None, recharges=None):
        self.title = title
        self.text = text
        self.uses = uses
        self.recharges = recharges

    def __str__(self):
        posttitletext = ""
        if self.recharges == None and self.uses == None:
            # It's an at-will feaure
            posttitletext = ""
        if self.recharges != None and self.uses == None:
            # Recharges on short or long rest
            posttitletext = " (Recharges on {self.recharges})"
        elif self.recharges == None and self.uses != None:
            # Does this actually ever happen? I think
            # uses implies recharges, because anything
            # without recharges implies at will, right?!?
            posttitletext = " ({self.uses})"
        elif self.recharges != None and self.uses != None:
            # Use N number of times, recharges at dawn (whatever)
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
            # light, two-handed, versatile, etc
        self.tohit = 0
        self.reach = "5ft."

    def __str__(self):
        text  = f"***{self.title}.*** *Melee Weapon Attack:* +{self.tohit} to hit, range {self.reach}, one target. "
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
        text  = f"***{self.title}.*** *Ranged Weapon Attack:* +{self.tohit} to hit, range {self.range}, one target. "
        text += f"Hit: {self.dmgamt} {self.dmgtype}"
        return text

class StatBlock:
    def __init__(self):
        pass

    def emitmd(self) -> str:
        return ""

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

    def choose(self, promptmsg : str, choices=None):
        if choices == None:
            return self.input(promptmsg)
        elif isinstance(choices, list):
            self.output(promptmsg)
            return self.choosefromlist(choices)
        elif isinstance(choices, dict):
            self.output(promptmsg)
            return self.choosefrommap(choices)
        else:
            error("WTF?!?", choices)

class TerminalInput(Input):
    def output(self, *values): print(*values)

    def input(self, prompt : str = "") -> str: return input(prompt + " >>> ")

class ScriptedInput(Input):
    def __init__(self, inputfile):
        self.inputfile = inputfile

    def output(self, *values): print(*values)

    def input(self, prompt : str = "") -> str: return input(prompt + ">>> ")

io = TerminalInput()

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
            # Access to a few useful Python packages
            "os": os,
            #"random": random,
            # Access to a few of the core Python builtins
            "int": int,
            "str": str,
            # Our roots-level modules
            "roots": roots,
            # Our I/O facilities
            "log": log,
            "warn": warn,
            "error": error,
            "print": io.output,
            "choose": io.choose,
            # Module facilities
            "getattr": getattr,
            "setattr": setattr,
            "parent": parent,
            "loadmodule": loadmodule,
            # Utility methods of our own
            "dieroll": dieroll,
            "randomfrom": randompick,
            "randomint": randomint,
            "randommodule": random,
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
# Main entrypoint
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
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbosity != None:
        if args.verbosity == 'verbose':
            verbose = True
        elif args.verbosity == 'quiet':
            quiet = True

    if args.savepy != None:
        SAVEPY = args.savepy
    
    # Load modules, have them bootstrap in turn
    loadrootmodule(REPOROOT + "Abilities")
    #loadrootmodule(REPOROOT + "Backgrounds")
    #loadrootmodule(REPOROOT + "Classes")
    loadrootmodule(REPOROOT + "Equipment")
    #loadrootmodule(REPOROOT + "Feats")
    loadrootmodule(REPOROOT + "Races")
    #loadrootmodule(REPOROOT + "Creatures") # <-- this will be an interesting day

    # Test zone
    #print(roots['Races'].random())
    #print(roots['Equipment'].weapons)
    #print(roots['Equipment'].armor)

    # Examine command line, let's see if we need to script-generate
    # our PC/NPC, or if we do it interactively.
    if args.scripts != None:
        for script in args.scripts:
            print("Processing",script)
            io = ScriptedInput(script)
    else:
        print("Run interactively!")

if __name__ == '__main__':
	main()
