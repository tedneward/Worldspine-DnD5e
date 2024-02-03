# Barbarian
Barbarians are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.

```
name = 'Barbarian'
description = "***Class: Barbarian.*** Barbarians are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength."
```

## Class features
As a barbarian, you gain the following class features.

Level|Proficiency Bonus|Rages|Rage Damage|Features
-----|-----------------|-----|-----------|--------
1st  |+2|2|+2|[Rage](#rage), [Unarmored Defense](#unarmored-defense)
2nd	 |+2|2|+2|[Reckless Attack](#reckless-attack)
3rd	 |+2|3|+2|[Primal Path](#primal-path)
4th	 |+2|3|+2|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)
5th	 |+3|3|+2|[Extra Attack](#extra-attack), [Instinctive Pounce](#instinctive-pounce)
6th	 |+3|4|+2|Path feature
7th	 |+3|4|+2|[Feral Instinct](#feral-instinct)
8th	 |+3|4|+2|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
9th	 |+4|4|+3|[Brutal Critical](#brutal-critical) (1 die)
10th |+4|4|+3|Path feature
11th |+4|4|+3|[Relentless Rage](#relentless-rage)
12th |+4|5|+3|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
13th |+5|5|+3|[Brutal Critical](#brutal-critical) (2 dice)
14th |+5|5|+3|Path feature
15th |+5|5|+3|[Persistent Rage](#persistent-rage)
16th |+5|5|+4|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
17th |+6|6|+4|[Brutal Critical](#brutal-critical) (3 dice)
18th |+6|6|+4|[Indomitable Might](#indomitable-might)
19th |+6|6|+4|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
20th |+6|Unlimited|+4|[Primal Champion](#primal-champion)

```
# Rages: [Rages, Rage Damage]
rages = {
    1: [2, "+2"],
    2: [2, "+2"],
    3: [3, "+2"],
    4: [3, "+2"],
    5: [3, "+2"],
    6: [4, "+2"],
    7: [4, "+2"],
    8: [4, "+2"],
    9: [4, "+3"],
    10:[4, "+3"],
    11:[4, "+3"],
    12:[5, "+3"],
    13:[5, "+3"],
    14:[5, "+3"],
    15:[5, "+3"],
    16:[5, "+4"],
    17:[6, "+4"],
    18:[6, "+4"],
    19:[6, "+4"],
    20:["Unlimited", "+4"],
}
```

### Hit Points
**Hit Dice**: 1d12 per barbarian level

**Hit Points at 1st Level**: 12 + your Constitution modifier

**Hit Points at Higher Levels**: 1d12 (or 7) + your Constitution modifier per barbarian level after 1st

```
def everylevel(npc): npc.hits('d12')

def level1(npc):
```

### Proficiencies
**Armor**: Light armor, medium armor, shields

**Weapons**: Simple weapons, martial weapons

**Tools**: None

**Saving Throws**: Strength, Constitution

**Skills**: Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival

```
    for arm in Equipment.armor['light'] | Equipment.armor['medium'] | Equipment.armor['shields']:
        npc.addproficiency(arm)
    for wpn in Equipment.weapons['all']: npc.addproficiency(wpn)

    npc.addproficiency("STR")
    npc.addproficiency("CON")

    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a greataxe or (b) any martial melee weapon
* (a) two handaxes or (b) any simple weapon
* An explorer's pack and four javelins

```
    npc.addequipment("Greataxe OR any martial melee weapon")
    npc.addequipment("Two handaxes OR any simple weapon")
    npc.addequipment("Four javelins")
    npc.addequipment("An explorer's pack")
```

## Rage
*1st-level barbarian feature*

In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.

While raging, you gain the following benefits if you aren't wearing heavy armor:

* You have advantage on Strength checks and Strength saving throws.
* When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
* You have resistance to bludgeoning, piercing, and slashing damage.

If you are able to cast spells, you can't cast them or concentrate on them while raging.

Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends, and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.

Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.

```
    class Rage(BonusAction):
        def __init__(self):
            BonusAction.__init__(self, "Rage", None, "long rest")
        
        def __str__(self):
            npclevels = self.npc.levels("Barbarian")
            numrages = rages[npclevels][0]
            ragedmg = rages[npclevels][1]

            if npclevels < 20:
                self.uses = numrages
            else:
                self.recharges = None

            self.text = f"You enter into a rage. While raging, you have advantage on Strength checks and Strength saving throws; when you make a melee weapon attack using Strength, you gain a {ragedmg} bonus to damage; and you have resistance to bludgeoning, piercing, and slashing damage. Your rage lasts for 1 minute."

            self.text += " If you are able to cast spells, you can't cast them or concentrate on them while raging."

            if npclevels < 15: 
                self.text += " It ends early if you fall unconscious or if your turn ends and you have not attacked a hostile creature since your last turn or taken damage since then."
            else: 
                self.text += " It ends early if you fall unconscious."

            self.text += " You can end your rage on your turn as a bonus action."

            if npclevels >= 7:
                self.text += " You can move up to half your speed as part of this bonus action."

            return BonusAction.__str__(self)

    npc.append(Rage())
```

## Unarmored Defense
*1st-level barbarian feature*

While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.

```
    npc.append(UnarmoredDefense("CON"))
```

## Survival Instincts
*2nd-level barbarian feature* 

You become proficient in your choice of two of the following skills: Animal Handling, Medicine, Nature, Perception, or Survival.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills.

```
def level2(npc):
    skill = choose("Choose a Survival Instinct: ", ['Animal Handling', 'Medicine', 'Nature', 'Perception', 'Survival'])
    npc.addexpertise(skill)
    skill = choose("Choose a Survival Instinct: ", ['Animal Handling', 'Medicine', 'Nature', 'Perception', 'Survival'])
    npc.addexpertise(skill)
```

## Reckless Attack
*2nd-level barbarian feature* 

You can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.

```
    npc.append(Action("Reckless Attack", "When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.") )
```

## Primal Path
At 3rd level, you choose a path that shapes the nature of your rage:

* [Berserker](./Berserker.md)
* [Totem Warrior](./TotemWarrior.md)

Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels.

```
def level3(npc):
    # Choose subclass
    npc.addsubclass(choose("Choose a Primal Path:", childmods))
```

## Primal Knowledge
*3rd-level optional barbarian feature*

When you reach 3rd level and again at 10th level, you gain proficiency in one skill of your choice from the list of skills available to barbarians at 1st level.

```
    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])

def level10(npc):
    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): choosefeatorasi(npc)
def level8(npc): choosefeatorasi(npc)
def level12(npc): choosefeatorasi(npc)
def level16(npc): choosefeatorasi(npc)
def level19(npc): choosefeatorasi(npc)
```

## Extra Attack
*5th-level barbarian feature* 

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
def level5(npc):
    npc.append(Multiattack())
```

## Instinctive Pounce
*5th-level barbarian feature*

When a creature ends its turn within 15 feet of you, you can use your reaction to move up to half your speed to a space closer to the creature. This movement doesn't provoke opportunity attacks.

```
    npc.append(Reaction("Instinctive Pounce", "When a creature ends its turn within 15 feet of you, you move up to half your speed to a space closer to the creature. This movement doesn't provoke opportunity attacks.") )
```

## Feral Instinct
*7th-level barbarian feature*

Your instincts are so honed that you have advantage on initiative rolls.

Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.

```
def level7(npc):
    npc.append(Feature("Feral Instinct", "You have advantage on initiative rolls. Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.") )
```

## Instinctive Pounce
*7th-level optional barbarian feature*

As part of the bonus action you take to enter your rage, you can move up to half your speed. 

## Brutal Critical
*9th-level barbarian feature*

Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.

This increases to two additional dice at 13th level and three additional dice at 17th level.

```
class BrutalCritical(Feature):
    def __init__(self):
        Feature.__init__(self, "Brutal Critical", "")
    
    def __str__(self):
        npclevels = self.npc.levels("Barbarian")
        if npclevels < 13:
            return f"***Brutal Critical.*** You roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack."
        elif npclevels < 17:
            return f"***Brutal Critical.*** You roll two additional weapon damage dice when determining the extra damage for a critical hit with a melee attack."
        else:
            return f"***Brutal Critical.*** You roll three additional weapon damage dice when determining the extra damage for a critical hit with a melee attack."

def level9(npc): npc.append(BrutalCritical())
```

## Relentless Rage
*11th-level barbarian feature*

Your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.

Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.

```
def level11(npc):
    npc.append(Feature("Relentless Rage", "If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. Each time you use this feature after the first, the DC increases by 5.", "short rest") )
```

## Persistent Rage
*15th-level barbarian feature*

Your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.

## Indomitable Might
*18th-level barbarian feature*

If your total for a Strength check is less than your Strength score, you can use that score in place of the total.

```
def level18(npc):
    npc.append(Feature("Indomitable Might", "If your total for a Strength check is less than your Strength score, you can use that score in place of the total.") )
```

## Primal Champion
*20th-level barbarian feature*

You embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.

```
def level20(npc):
    npc.STR += 4
    npc.CON += 4
```