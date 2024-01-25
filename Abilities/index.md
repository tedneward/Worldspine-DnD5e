# Generating Ability Scores

There are as many different ways to roll ability scores as there are DMs.

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
def randomgen():
    abilities = {}

    abilities['STR'] = randomint(3,18)
    abilities['DEX'] = randomint(3,18)
    abilities['CON'] = randomint(3,18)
    abilities['INT'] = randomint(3,18)
    abilities['WIS'] = randomint(3,18)
    abilities['CHA'] = randomint(3,18)

    return abilities
```

## Random: 4d6 seven times
4d6, throwing out lowest d6 each time, seven times throwing out lowest score 

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
    "Average": average
    "Hand": handentry, 
    "NPC": npcstandard, 
    "Randomgen": randomgen, 
    "Standard": standard, 
}

# All the skills that players may use to affect their ability checks
skills = [ 
    'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
    'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
    'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
    'Religion', 'Sleight of Hand', 'Stealth', 'Survival'
]

def random():
    return randomgen()
```
