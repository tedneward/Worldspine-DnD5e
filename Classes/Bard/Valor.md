# Bardic College: College of Valor
Bards of the College of Valor are daring skalds whose tales keep alive the memory of the great heroes of the past, and thereby inspire a new generation of heroes. These bards gather in mead halls or around great bonfires to sing the deeds of the mighty, both past and present. They travel the land to witness great events firsthand and to ensure that the memory of those events doesn't pass from the world. With their songs, they inspire others to reach the same heights of accomplishment as the heroes of old.

```
name = 'College of Valor'
description = "***Bardic College: College of Valor.*** Bards of the College of Valor are daring skalds whose tales keep alive the memory of the great heroes of the past, and thereby inspire a new generation of heroes. These bards gather in mead halls or around great bonfires to sing the deeds of the mighty, both past and present. They travel the land to witness great events firsthand and to ensure that the memory of those events doesn't pass from the world. With their songs, they inspire others to reach the same heights of accomplishment as the heroes of old."
```

## Bonus Proficiencies
*3rd-level College of Valor feature*

You gain proficiency with medium armor, shields, and martial weapons.

```
def level3(npc):
    for arm in Equipment.armor['medium'] | Equipment.armor['shields']: 
        npc.addproficiency(arm)
    for wpn in Equipment.weapons['martial']: 
        npc.addproficiency(wpn)
```

## Combat Inspiration
*3rd-level College of Valor feature*

You learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses.

```
    npc.append(Feature("Combat Inspiration", "A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses.") )
```

## Extra Attack
*6th-level College of Valor feature*

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
def level6(npc):
    npc.append(Multiattack())
```

## Battle Magic
*14th-level College of Valor feature*

You have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action.

```
def level14(npc):
    npc.append(BonusAction("Battle Magic", "When you use your action to cast a bard spell, you make one weapon attack.") )
```
