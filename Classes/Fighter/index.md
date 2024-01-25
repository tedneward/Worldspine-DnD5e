# Fighter
Questing knights, conquering overlords, royal champions, elite foot soldiers, hardened mercenaries, and bandit kings — as fighters, they all share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. And they are well acquainted with death, both meting it out and staring it defiantly in the face.

***Well-Rounded Specialists.*** Fighters learn the basics of all combat styles. Every fighter can swing an axe, fence with a rapier, wield a longsword or a greatsword, use a bow, and even trap foes in a net with some degree of skill. Likewise, a fighter is adept with shields and every form of armor. Beyond that basic degree of familiarity, each fighter specializes in a certain style of combat. Some concentrate on archery, some on fighting with two weapons at once, and some on augmenting their martial skills with magic. This combination of broad general ability and extensive specialization makes fighters superior combatants on battlefields and in dungeons alike.

***Trained for Danger.*** Not every member of the city watch, the village militia, or the queen’s army is a fighter. Most of these troops are relatively untrained soldiers with only the most basic combat knowledge. Veteran soldiers, military officers, trained bodyguards, dedicated knights, and similar figures are fighters.

Some fighters feel drawn to use their training as adventurers. The dungeon delving, monster slaying, and other dangerous work common among adventurers is second nature for a fighter, not all that different from the life he or she left behind. There are greater risks, perhaps, but also much greater rewards — few fighters in the city watch have the opportunity to discover a magic flame tongue sword, for example.

```
name = 'Fighter'
description = "***Class: Fighter.*** Questing knights, conquering overlords, royal champions, elite foot soldiers, hardened mercenaries, and bandit kings — as fighters, they all share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. And they are well acquainted with death, both meting it out and staring it defiantly in the face."
dependencies = ['Maneuvers.md', 'Styles.md']
```

Level|Proficiency Bonus|traits
-----|-----------------|--------
1st|+2|[Fighting Style](#fighting-style), [Second Wind](#second-wind)
2nd|+2|[Action Surge](#action-surge) (x1)
3rd|+2|[Martial Archetype](#martial-archetype)
4th|+2|[Ability Score Improvement](#ability-score-improvement)
5th|+3|[Extra Attack](#extra-attack) (x1)
6th|+3|[Ability Score Improvement](#ability-score-improvement)
7th|+3|[Martial Archetype feature](#martial-archetype)
8th|+3|[Ability Score Improvement](#ability-score-improvement)
9th|+4|[Indomitable](#indomitable) (x1)
10th|+4|[Martial Archetype feature](#martial-archetype)
11th|+4|[Extra Attack](#extra-attack) (x2)
12th|+4|[Ability Score Improvement](#ability-score-improvement)
13th|+5|[Indomitable](#indomitable) (x2)
14th|+5|[Ability Score Improvement](#ability-score-improvement)
15th|+5|[Martial Archetype feature](#martial-archetype)
16th|+5|[Ability Score Improvement](#ability-score-improvement)
17th|+6|[Action Surge](#action-surge) (x2), [Indomitable](#indomitable) (x3)
18th|+6|[Martial Archetype feature](#martial-archetype)
19th|+6|[Ability Score Improvement](#ability-score-improvement)
20th|+6|[Extra Attack](#extra-attack) (x3)

As a fighter, you gain the following class traits.

## Hit Points
**Hit Dice**: 1d10 per fighter level

**Hit Points at 1st Level**: 10 + your Constitution modifier

**Hit Points at Higher Levels**: 1d10 (or 6) + your Constitution modifier per fighter level after 1st

```
def everylevel(npc): npc.hits('d10')
```

## Proficiencies
**Armor**: All armor, shields

**Weapons**: Simple weapons, martial weapons

**Tools**: None

**Saving Throws**: Strength, Constitution

**Skills**: Choose two skills from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival

Equipment

* (a) chain mail or (b) leather, longbow, and 20 arrows
* (a) a martial weapon and a shield or (b) two martial weapons
* (a) a light crossbow and 20 bolts or (b) two handaxes
* (a) a dungeoneer's pack or (b) an explorer's pack

```
def level1(npc):
    npc.savingthrows.append("STR")
    npc.savingthrows.append("CON")

    for arm in armor['light'] | armor['medium'] | armor['heavy'] | armor['shields']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['martial-melee'] | weapons['simple-ranged'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)

    skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    chooseskill(npc, skills)
    chooseskill(npc, skills)

    npc.equipment.append("Martial weapon")
    npc.equipment.append("Shield OR martial weapon")
    npc.equipment.append("Light crossbow and 20 bolts OR two handaxes")
    npc.equipment.append("Dungeoneer's pack, or explorer's pack")
    npc.armorclass['Chain mail'] = 16
```

## Fighting Style
*1st-level fighter feature* 

You adopt a particular style of fighting as your specialty. Choose one of the [styles](Styles.md) available. You can't take a Fighting Style option more than once, even if you later get to choose again.

```
    choosestyle(npc)
    #style = choose("Choose a Fighting Style:", styles)
    #npc.fightingstyle = style[0]
    #(style[1])(npc)
```

## Second Wind
You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.

Once you use this feature, you must finish a short or long rest before you can use it again.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Second Wind (Recharges on short or long rest).*** On your turn, you can regain 1d10 + {npc.levels('Fighter')} hit points."))
```


## Action Surge
Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action.

Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.

```
def level2(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Action Surge ({'2/' if npc.levels('Fighter') > 16 else ''}Recharges on short or long rest).*** On your turn, you can take one additional action on top of your regular action and a possible bonus action."))
```

## Martial Archetype
At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques:

* [Champion](Champion.md)

The archetype you choose grants you traits at 3rd level and again at 7th, 10th, 15th, and 18th level.

```
def level3(npc):
    # Choose subclass
    (_, subclass) = choose("Choose a Martial Archetype:", subclasses)
    npc.subclasses[root['Classes']['Fighter']] = subclass
    npc.description.append(subclass.description)
```

## Ability Score Improvement
When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level6(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level14(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

### Martial Versatility
Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, as you shift the focus of your martial practice:

* Replace a fighting style you know with another fighting style available to fighters.
* If you know any maneuvers from the [Battle Master](BattleMaster.md) archetype, you can replace one maneuver you know with a different maneuver. 

## Extra Attack
*5th-level Fighter feature*

You can attack twice, instead of once, whenever you take the Attack action on your turn.

The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class.

```
def level5(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Multiattack.*** You can attack {'twice' if npc.levels('Fighter') < 11 else '3 times' if npc.levels('Fighter') < 20 else 'four times'} whenever you take the Attack action on your turn."))
```

## Indomitable
*9th-level Fighter feature*

You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.

You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.

```
def level9(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Indomitable ({'' if npc.levels('Fighter') < 13 else '2/' if npc.levels('Fighter') < 17 else '3/'}Recharges on long rest).*** You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest."))
```
