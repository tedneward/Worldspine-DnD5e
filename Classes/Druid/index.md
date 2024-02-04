# Druid
Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature’s resilience, cunning, and fury. They claim no mastery over nature. Instead, they see themselves as extensions of nature’s indomitable will.

## Power of Nature
Druids revere nature above all, gaining their spells and other magical powers either from the force of nature itself or from a nature deity. Many druids pursue a mystic spirituality of transcendent union with nature rather than devotion to a divine entity, while others serve gods of wild nature, animals, or elemental forces. The ancient druidic traditions are sometimes called the Old Faith, in contrast to the worship of gods in temples and shrines.

Druid spells are oriented toward nature and animals — the power of tooth and claw, of sun and moon, of fire and storm. Druids also gain the ability to take on animal forms, and some druids make a particular study of this practice, even to the point where they prefer animal form to their natural form.

## Preserve the Balance
For druids, nature exists in a precarious balance. The four elements that make up a world — air, earth, fire, and water — must remain in equilibrium. If one element were to gain power over the others, the world could be destroyed, drawn into one of the elemental planes and broken apart into its component elements. Thus, druids oppose cults of Elemental Evil and others who promote one element to the exclusion of others.

Druids are also concerned with the delicate ecological balance that sustains plant and animal life, and the need for civilized folk to live in harmony with nature, not in opposition to it. Druids accept that which is cruel in nature, and they hate that which is unnatural, including aberrations (such as beholders and mind flayers) and undead (such as zombies and vampires). Druids sometimes lead raids against such creatures, especially when the monsters encroach on the druids’ territory.

Druids are often found guarding sacred sites or watching over regions of unspoiled nature. But when a significant danger arises, threatening nature’s balance or the lands they protect, druids take on a more active role in combating the threat, as adventurers.

*You must have a Wisdom score of 13 or higher in order to multiclass in or out of this class.*

```
name = 'Druid'
description = "***Class: Druid.*** Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will."
```

## Class features
As a druid, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|2|2|-|-|-|-|-|-|-|-|[Druidic](#druidic), [Spellcasting](#spellcasting)
2nd  |+2|2|3|-|-|-|-|-|-|-|-|[Wild Shape](#wild-shape), [Druid Circle](#druid-circle)
3rd  |+2|2|4|2|-|-|-|-|-|-|-|
4th  |+2|3|4|3|-|-|-|-|-|-|-|[Wild Shape](#wild-shape) improvement, [Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
5th  |+3|3|4|3|2|-|-|-|-|-|-|
6th  |+3|3|4|3|3|-|-|-|-|-|-|Druid Circle feature
7th  |+3|3|4|3|3|1|-|-|-|-|-|
8th  |+3|3|4|3|3|2|-|-|-|-|-|[Wild Shape](#wild-shape) improvement, [Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
9th  |+4|3|4|3|3|3|1|-|-|-|-|
10th |+4|4|4|3|3|3|2|-|-|-|-|Druid Circle feature
11th |+4|4|4|3|3|3|2|1|-|-|-|
12th |+4|4|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|4|4|3|3|3|2|1|1|-|-|
14th |+5|4|4|3|3|3|2|1|1|-|-|Druid Circle feature
15th |+5|4|4|3|3|3|2|1|1|1|-|
16th |+5|4|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|4|4|3|3|3|2|1|1|1|1|
18th |+6|4|4|3|3|3|3|1|1|1|1|[Timeless Body](#timeless-body), [Beast Shapes](#beast-shapes)
19th |+6|4|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|4|4|3|3|3|3|2|2|1|1|[Archdruid](#archdruid)

```
cantriptable = {
    1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4,
    11: 4, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4,
}
```

### Hit Points
**Hit Dice**: 1d8 per druid level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per druid level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)

**Weapons**: Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears

**Tools**: Herbalism kit

**Saving Throws**: Intelligence, Wisdom

**Skills**: Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival

```
def level1(npc):
    for arm in Equipment.armor['light'] | Equipment.armor['medium'] | Equipment.armor['shields']: 
        npc.addproficiency(arm)

    for wpn in ['Club','Dagger','Dart','Javelin','Mace','Quarterstaff','Scimitar','Sickle','Sling','Spear']:
        npc.addproficiency(Equipment.weapons['all'][wpn])

    npc.addproficiency('WIS')
    npc.addproficiency('INT')

    druidskills = ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival']
    chooseskill(npc, druidskills)
    chooseskill(npc, druidskills)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a wooden shield or (b) any simple weapon
* (a) a scimitar or (b) any simple melee weapon
* Leather armor, an explorer's pack, and a druidic focus

```
    npc.equipment.append(Equipment.armor['all']['Leather armor'])
    npc.equipment.append("Explorer's pack")
    npc.equipment.append("Druidic focus")

    npc.equipment.append("Shield (wood) OR any simple weapon")
    npc.equipment.append("Scimitar OR any simple melee weapon")
```

### Druidic
You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic.

```
    npc.languages.append("Druidic")
```

## Spellcasting
*1st-level druid feature*

Drawing on the divine essence of nature itself, you can cast spells to shape that essence to your will.

### Cantrips
You know two cantrips of your choice from the druid spell list. You learn additional druid cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Druid table.

### Preparing and Casting Spells
The Druid table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these druid spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of druid spells that are available for you to cast, choosing from the druid spell list. (Note that at the DM's discretion, the list of druid spells available for preparation may not be the entire list of druid spells in the world.) When you do so, choose a number of druid spells equal to your Wisdom modifier + your Druid level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you are a 3rd-level druid, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

### Spellcasting Ability
Wisdom is your spellcasting ability for your druid spells, since your magic draws upon your devotion and attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a druid spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

### Ritual Casting
You can cast a druid spell as a ritual if that spell has the ritual tag and you have the spell prepared.

### Spellcasting Focus
You can use a druidic focus as a spellcasting focus for your druid spells.

```
    spellcasting = DivineSpellcasting("Druid", cantriptable)
    npc.append(spellcasting)
```

## Wild Shape
*2nd-level druid feature*

You can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.

Your druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed.

**Beast Shapes**

Level | Max. CR | Limitations | Example
----- | ------- | ----------- | --------
2nd   | 1/4     | No flying or swimming speed | Wolf
4th   | 1/2     | No flying speed | Crocodile
8th   |  1      | - | Giant eagle

You can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.

While you are transformed, the following rules apply:

* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.

* When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.

* You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.

* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.

* You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.

```
class WildShape(Action):
    def __init__(self):
        Action.__init__(self, "Wild Shape", "", "short rest", "2")

    def evaltext(self): return ""

    def apply(self):
        npclevels = self.npc.levels("Druid")

        beastcr = ""
        beastmove = ""
        if npclevels < 4: 
            beastcr = "1/4"
            beastmove = " that has no flying or swimming speed"
        elif npclevels < 8: 
            beastcr = "1/2"
            beastmove = " that has no flying speed"
        else:
            beastcr = "1"
            beastmove = ""

        self.text = "You can magically assume the shape of a beast that you have seen before. You can transform into any beast that has a challenge rating of " + beastcr + " or lower" + beastmove + ". You can stay in a beast shape for " + str(npclevels // 2) + " hours. You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.\n"

        self.text += """
While you are transformed, the following rules apply:

* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.

* When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.

* You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.

* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.

* You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.
        """

def level2(npc): 
    npc.append(WildShape())
```

## Wild Companion
*2nd-level druid feature*

You gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the [find familiar](../../Magic/Spells/find-familiar.md) spell, without material components.

When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your druid level.

```
    npc.append(Action("Wild Companion", "You expend a use of your Wild Shape to cast {spelllink('find familiar')}, without material components. When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after {(self.npc.levels('Druid') + 1) // 2} hours.") )
```

## Druid Circle
At 2nd level, you choose to identify with a circle of druids:

* [Circle of the Land](Land.md)
* [Circle of the Moon](Moon.md)

Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level.

```
    circlemod = choose("Choose a Druidic Circle:", childmods)
    npc.addsubclass(circlemod)

    # Bring domain spells into Spellcasting
    if getattr(circlemod, "circlespells", None) != None:
        spellcasting.addspellspreparedtable(circlemod.circlespells)
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

## Cantrip Versatility
*4th-level druid feature*

Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the druid spell list. 

## Timeless Body
*18th-level druid feature*

The primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.

```
def level18(npc):
    npc.append(Feature("Timeless Body", "The primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.") )
```

## Beast Shapes
*18th-level druid feature*

You can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components.

```
    npc.append(Feature("Beast Shapes", "You can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components.") )
```

## Archdruid
*20th-level druid feature*

You can use your Wild Shape an unlimited number of times.
