# Roguish Archetype: Arcane Trickster
Some rogues enhance their fine-honed skills of stealth and agility with magic, learning tricks of enchantment and illusion. These rogues include pickpockets and burglars, but also pranksters, mischief-makers, and a significant number of adventurers.

```
name = 'Arcane Trickseter'
description = "***Roguish Archetype: Arcane Trickster.*** Some rogues enhance their fine-honed skills of stealth and agility with magic, learning tricks of enchantment and illusion. These rogues include pickpockets and burglars, but also pranksters, mischief-makers, and a significant number of adventurers."
```


## Arcane Trickster Spellcasting
*3rd-level Arcane Trickster feature*

You augment your roguish prowess with the ability to cast spells.

### Cantrips
You learn three cantrips: [mage hand](../../Magic/Spells/mage-hand.md) and two other cantrips of your choice from the wizard spell list. You learn another wizard cantrip of your choice at 10th level.

### Spell Slots
The Arcane Trickster Spellcasting table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

Rogue Level|Cantrips Known|Spells Known|1st|2nd|3rd|4th
-------------|--------------|------------|---|---|---|---
3rd|Mage Hand + 2|3|2|-|-|-
4th|Mage Hand + 2|4|3|-|-|-
5th|Mage Hand + 2|4|3|-|-|-
6th|Mage Hand + 2|4|3|-|-|-
7th|Mage Hand + 2|5|4|2|-|-
8th|Mage Hand + 2|6|4|2|-|-
9th|Mage Hand + 2|6|4|2|-|-
10th|Mage Hand + 3|7|4|3|-|-
11th|Mage Hand + 3|8|4|3|-|-
12th|Mage Hand + 3|8|4|3|-|-
13th|Mage Hand + 3|9|4|3|2|-
14th|Mage Hand + 3|10|4|3|2|-
15th|Mage Hand + 3|10|4|3|2|-
16th|Mage Hand + 3|11|4|3|3|-
17th|Mage Hand + 3|11|4|3|3|-
18th|Mage Hand + 3|11|4|3|3|-
19th|Mage Hand + 3|12|4|3|3|1
20th|Mage Hand + 3|13|4|3|3|1

### Spells Known of 1st Level and Higher
You know three 1st-level wizard spells of your choice, two of which you must choose from the enchantment and illusion spells on the wizard spell list.

The Spells Known column of the Arcane Trickster Spellcasting table shows when you learn more wizard spells of 1st level or higher. Each of these spells must be an enchantment or illusion spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the wizard spells you know with another spell of your choice from the wizard spell list. The new spell must be of a level for which you have spell slots, and it must be an enchantment or illusion spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level from any school of magic.

### Spellcasting Ability
Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Intelligence modifier

**Spell attack modifier** = your proficiency bonus + your Intelligence modifier

```
def level3(npc):
    spellcasting = halfcaster(npc, 'INT', name)
    spellcasting.casterclass = allclasses['Rogue']

    spellcasting.cantripsknown.append("mage hand")
    spellcasting.maxcantripsknown = 3
    spellcasting.maxspellsknown = 3

def level4(npc):
    npc.spellcasting[name].maxspellsknown = 4

def level7(npc):
    npc.spellcasting[name].maxspellsknown = 5

def level8(npc):
    npc.spellcasting[name].maxspellsknown = 6

def level10(npc):
    npc.spellcasting[name].maxcantripsknown = 4
    npc.spellcasting[name].maxspellsknown = 7

def level11(npc):
    npc.spellcasting[name].maxspellsknown = 8

def level13(npc):
    npc.spellcasting[name].maxspellsknown = 9

def level14(npc):
    npc.spellcasting[name].maxspellsknown = 10

def level16(npc):
    npc.spellcasting[name].maxspellsknown = 11

def level19(npc):
    npc.spellcasting[name].maxspellsknown = 12

def level20(npc):
    npc.spellcasting[name].maxspellsknown = 13
```

## Mage Hand Legerdemain
*3rd-level Arcane Trickster feature*

When you cast [mage hand](../../Magic/Spells/mage-hand.md), you can make the spectral hand invisible, and you can perform the following additional tasks with it:

* You can stow one object the hand is holding in a container worn or carried by another creature.

* You can retrieve an object in a container worn or carried by another creature.

* You can use thieves' tools to pick locks and disarm traps at range.

You can perform one of these tasks without being noticed by a creature if you succeed on a Dexterity (Sleight of Hand) check contested by the creature's Wisdom (Perception) check.

In addition, you can use the bonus action granted by your Cunning Action to control the hand.

```
    npc.traits.append("***Mage Hand Legerdemain.*** When you cast [mage hand](../../Magic/Spells/mage-hand.md), you can make the spectral hand invisible, and you can perform the following additional tasks with it: (1) You can stow one object the hand is holding in a container worn or carried by another creature. (2) You can retrieve an object in a container worn or carried by another creature. (3) You can use thieves' tools to pick locks and disarm traps at range. You can perform one of these tasks without being noticed by a creature if you succeed on a Dexterity (Sleight of Hand) check contested by the creature's Wisdom (Perception) check. In addition, you can use the bonus action granted by your Cunning Action to control the hand.")
```

## Magical Ambush
*9th-level Arcane Trickster feature*

If you are hidden from a creature when you cast a spell on it, the creature has disadvantage on any saving throw it makes against the spell this turn.

```
def level9(npc):
    npc.traits.append("***Magical Ambush.*** If you are hidden from a creature when you cast a spell on it, the creature has disadvantage on any saving throw it makes against the spell this turn.")
```

## Versatile Trickster
*11th-level Arcane Trickster feature*

You gain the ability to distract targets with your [mage hand](../../Magic/Spells/mage-hand.md). As a bonus action on your turn, you can designate a creature within 5 feet of the spectral hand created by the spell. Doing so gives you advantage on attack rolls against that creature until the end of the turn.

```
def level11(npc):
    npc.bonusactions.append("***Versatile Trickster.*** You can designate a creature within 5 feet of the spectral hand created by the *mage hand* spell; doing so gives you advantage on attack rolls against that creature until the end of the turn.")
```

## Spell Thief
*17th-level Arcane Trickster feature*

You gain the ability to magically steal the knowledge of how to cast a spell from another spellcaster.

Immediately after a creature casts a spell that targets you or includes you in its area of effect, you can use your reaction to force the creature to make a saving throw with its spellcasting ability modifier. The DC equals your spell save DC. On a failed save, you negate the spell's effect against you, and you steal the knowledge of the spell if it is at least 1st level and of a level you can cast (it doesn't need to be a wizard spell). For the next 8 hours, you know the spell and can cast it using your spell slots. The creature can't cast that spell until the 8 hours have passed.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level17(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Spell Thief (Recharges on long rest).*** Immediately after a creature casts a spell that targets you or includes you in its area of effect, you can use your reaction to force the creature to make a DC {npc.spellcasting[name].spellsavedc()} saving throw with its spellcasting ability modifier. On a failed save, you negate the spell's effect against you, and you steal the knowledge of the spell if it is at least 1st level and of a level you can cast (it doesn't need to be a wizard spell). For the next 8 hours, you know the spell and can cast it using your spell slots. The creature can't cast that spell until the 8 hours have passed."))
```
