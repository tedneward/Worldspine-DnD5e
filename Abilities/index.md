# Generating Ability Scores

There are as many different ways to roll ability scores as there are DMs.

```
name = "Abilities"
```

## Hand-Entry

```
def handentry():
    abilities = {}
    
    def numberorrandom(ability):
        maybe = choose(ability)
        if maybe == "random":
            return randomint(3,18)
        else:
            return int(maybe)
        
    abilities['STR'] = numberorrandom("STR")
    abilities['DEX'] = numberorrandom("DEX")
    abilities['CON'] = numberorrandom("CON")
    abilities['INT'] = numberorrandom("INT")
    abilities['WIS'] = numberorrandom("WIS")
    abilities['CHA'] = numberorrandom("CHA")

    return abilities
```

## Random: 3d6 six times

```
def threedsixrandomgen():
    abilities = {}

    abilities['STR'] = randomint(1,6) + randomint(1,6) + randomint(1,6)
    abilities['DEX'] = randomint(1,6) + randomint(1,6) + randomint(1,6)
    abilities['CON'] = randomint(1,6) + randomint(1,6) + randomint(1,6)
    abilities['INT'] = randomint(1,6) + randomint(1,6) + randomint(1,6)
    abilities['WIS'] = randomint(1,6) + randomint(1,6) + randomint(1,6)
    abilities['CHA'] = randomint(1,6) + randomint(1,6) + randomint(1,6)

    return abilities
```

## Random: 4d6 seven times
4d6, throwing out lowest d6 each time, seven times throwing out lowest score 

```
def fourdsevenrandomgen():
    def dieframe():
        frame = []
        for _ in range(0,4): frame.append(randomint(1,6))
        frame.sort()
        frame.reverse()
        return frame

    def sevenrolls():
        stats = []
        for _ in range(0,7):
            frame = dieframe()
            stats.append(frame.pop(0) + frame.pop(0) + frame.pop(0))
        stats.sort()
        stats.reverse()
        return stats

    abilities = {}

    scores = sevenrolls()
    stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    while len(stats) > 0:
        print(f"You have {scores} to assign")
        stat = choose(f"Apply the {scores[0]}: ", stats)
        abilities[stat] = scores[0]
        scores.pop(0)
        stats.remove(stat)

    return abilities
```

## Average
11s across the board, baby

```
def average():
    abilities = {}
    
    abilities['STR'] = 11
    abilities['DEX'] = 11
    abilities['CON'] = 11
    abilities['INT'] = 11
    abilities['WIS'] = 11
    abilities['CHA'] = 11

    return abilities
```

## Standard PC generation
15, 14, 13, 12, 10, 8, applied to your choice of stats

```
def standard():
    abilities = {}

    scores = [15, 14, 13, 12, 10, 8]
    stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    while len(stats) > 0:
        stat = choose(f"Apply the {scores[0]}: ", stats)
        abilities[stat] = scores[0]
        scores.pop(0)
        stats.remove(stat)

    return abilities
```

## Boosted Standard, for NPCs
16, 15, 12, 12, 12, 8, applied to your choice of stats

... to give those NPCs a little extra kick.

```
def npcstandard():
    abilities = {}

    scores = [16, 15, 12, 12, 12, 8]
    stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    while len(stats) > 0:
        stat = choose(f"Apply the {scores[0]}: ", stats)
        abilities[stat] = scores[0]
        scores.pop(0)
        stats.remove(stat)

    return abilities
```

```
methods = {
    "Average": average,
    "Hand": handentry, 
    "NPCStandard": npcstandard, 
    "Standard": standard, 
    "ThreeDSixRandomgen": threedsixrandomgen, 
    "FourDSevenRandomgen": fourdsevenrandomgen, 
}
```

## Ability Increases
Characters are often able to increase one or more of their ability scores one or more times. Details will depend (most often) on the class the character is leveling into.

Normally, no ability score can be increased beyond 20.

```
def chooseability(abilities=['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']):
    return choose("Choose an ability score: ", abilities)

def abilityscoreincrease(npc, abilities=['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']):
    chosen = choose("Choose an ability score to increase: ", abilities)
    if npc.getability(chosen) >= 20:
        warn("Increasing ability score",chosen,"takes it beyond 20!")
    npc.setability(chosen, npc.getability(chosen) + 1)
    return chosen
```


## Skills
Skills are proficiencies that add to a character's ability check or save.

* Acrobatics (DEX): 
* Animal Handling (WIS): 
* Arcana (INT): 
* Athletics (STR):
* Deception (CHA): 
* History (INT): 
* Insight (WIS): 
* Intimidation (CHA): 
* Investigation (INT):
* Medicine (WIS): 
* Nature (INT): 
* Perception (WIS): 
* Performance (CHA): 
* Persuasion (CHA):
* Religion (INT): 
* Sleight of Hand (DEX): 
* Stealth (DEX): 
* Survival (WIS):

```
# All the skills that players may use to affect their ability checks
skills = [ 
    'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
    'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
    'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
    'Religion', 'Sleight of Hand', 'Stealth', 'Survival'
]
def skilllist(): 
    return skills

skillability = { 
    'Acrobatics':'DEX',
    'Animal Handling':'WIS', 
    'Arcana':'INT',
    'Athletics':'STR',
    'Deception':'CHA',
    'History':'INT',
    'Insight':'WIS',
    'Intimidation':'CHA', 
    'Investigation':'INT',
    'Medicine':'WIS',
    'Nature':'INT',
    'Perception':'WIS', 
    'Performance':'CHA', 
    'Persuasion':'CHA',
    'Religion':'INT',
    'Sleight of Hand':'DEX', 
    'Stealth':'DEX',
    'Survival':'WIS'
}
def abilityforskill(skillname): 
    return skillability[skillname]

def chooseskill(npc, availableskills = skills): 
    srclist = availableskills
    for skill in srclist:
        if skill in npc.proficiencies:
            srclist.remove(skill)
    chosen = choose("Choose a skill: ", srclist)
    npc.addproficiency(chosen)
```

```
def random(npc):
    (fnname, fn) = randomfrom(methods)
    while fnname == 'Hand':
        (fnname, fn) = randomfrom(methods)
    abilities = fn()
    print("I rolled",abilities," as stats using", fnname, "for you, boss!")

    npc.addabilities(abilities)
```

```
exports = [ chooseability, abilityscoreincrease, skilllist, abilityforskill, chooseskill ]
```
