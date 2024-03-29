# Bard
Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds.

## Music and Magic
In the worlds of D&D, words and music are not just vibrations of air, but vocalizations with power all their own. The bard is a master of song, speech, and the magic they contain. Bards say that the multiverse was spoken into existence, that the words of the gods gave it shape, and that echoes of these primordial Words of Creation still resound throughout the cosmos. The music of bards is an attempt to snatch and harness those echoes, subtly woven into their spells and powers.

The greatest strength of bards is their sheer versatility. Many bards prefer to stick to the sidelines in combat, using their magic to inspire their allies and hinder their foes from a distance. But bards are capable of defending themselves in melee if necessary, using their magic to bolster their swords and armor. Their spells lean toward charms and illusions rather than blatantly destructive spells. They have a wide-ranging knowledge of many subjects and a natural aptitude that lets them do almost anything well. Bards become masters of the talents they set their minds to perfecting, from musical performance to esoteric knowledge.

## Learning from Experience
True bards are not common in the world. Not every minstrel singing in a tavern or jester cavorting in a royal court is a bard. Discovering the magic hidden in music requires hard study and some measure of natural talent that most troubadours and jongleurs lack. It can be hard to spot the difference between these performers and true bards, though. A bard’s life is spent wandering across the land gathering lore, telling stories, and living on the gratitude of audiences, much like any other entertainer. But a depth of knowledge, a level of musical skill, and a touch of magic set bards apart from their fellows.

Only rarely do bards settle in one place for long, and their natural desire to travel — to find new tales to tell, new skills to learn, and new discoveries beyond the horizon — makes an adventuring career a natural calling. Every adventure is an opportunity to learn, practice a variety of skills, enter long-forgotten tombs, discover lost works of magic, decipher old tomes, travel to strange places, or encounter exotic creatures. Bards love to accompany heroes to witness their deeds firsthand. A bard who can tell an awe-inspiring story from personal experience earns renown among other bards. Indeed, after telling so many stories about heroes accomplishing mighty deeds, many bards take these themes to heart and assume heroic roles themselves.

```
name = 'Bard'
description = "***Class: Bard.*** Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the magic they contain."
```

## Class Features
As a bard, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|Spells Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|------------|---|---|---|---|---|---|---|---|---|--------
 1st |+2|2| 4|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Bardic Inspiration](#bardic-inspiration) (d6)
 2nd |+2|2| 5|3|-|-|-|-|-|-|-|-|[Jack of All Trades](#jack-of-all-trades), [Song of Rest](#song-of-rest) (d6)
 3rd |+2|2| 6|4|2|-|-|-|-|-|-|-|[Bard College](#bard-college), [Expertise](#expertise)
 4th |+2|3| 7|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
 5th |+3|3| 8|4|3|2|-|-|-|-|-|-|[Bardic Inspiration](#bardic-inspiration) (d8), [Font of Inspiration](#font-of-inspiration)
 6th |+3|3| 9|4|3|3|-|-|-|-|-|-|[Countercharm](#countercharm), [Bard College](#bard-college) feature
 7th |+3|3|10|4|3|3|1|-|-|-|-|-|
 8th |+3|3|11|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
 9th |+4|3|12|4|3|3|3|1|-|-|-|-|[Song of Rest](#song-of-rest) (d8)
10th |+4|4|14|4|3|3|3|2|-|-|-|-|[Bardic Inspiration](#bardic-inspiration) (d10), [Expertise](#expertise), [Magical Secrets](#magical-secrets)
11th |+4|4|15|4|3|3|3|2|1|-|-|-|
12th |+4|4|15|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|4|16|4|3|3|3|2|1|1|-|-|[Song of Rest](#song-of-rest) (d10)
14th |+5|4|18|4|3|3|3|2|1|1|-|-|[Magical Secrets](#magical-secrets), [Bard College](#bard-college) feature
15th |+5|4|19|4|3|3|3|2|1|1|1|-|[Bardic Inspiration](#bardic-inspiration) (d12)
16th |+5|4|19|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|4|20|4|3|3|3|2|1|1|1|1|[Song of Rest](#song-of-rest) (d12)
18th |+6|4|22|4|3|3|3|3|1|1|1|1|[Magical Secrets](#magical-secrets)
19th |+6|4|22|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|4|22|4|3|3|3|3|2|2|1|1|[Superior Inspiration](#superior-inspiration)

### Hit Points
**Hit Dice**: 1d8 per bard level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per bard level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor

**Weapons**: Simple weapons, hand crossbows, longswords, rapiers, shortswords

**Tools**: Three musical instruments of your choice

**Saving Throws**: Dexterity, Charisma

**Skills**: Choose any three

```
def level1(npc):
    npc.addproficiency("DEX")
    npc.addproficiency("CHA")

    for arm in Equipment.armor['light']: npc.addproficiency(arm)
    for wpn in Equipment.weapons['simple']: npc.addproficiency(wpn)
    npc.addproficiency(Equipment.weapons['ranged']['Hand crossbow'].name)
    npc.addproficiency(Equipment.weapons['melee']['Longsword'].name)
    npc.addproficiency(Equipment.weapons['melee']['Shortsword'].name)
    npc.addproficiency(Equipment.weapons['melee']['Rapier'].name)

    for _ in range(0,3):
        npc.addproficiency(choose("Choose an instrument: ", Equipment.tools['musical']))

    chooseskill(npc)
    chooseskill(npc)
    chooseskill(npc)

    print(npc.getskills(False))
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a rapier, (b) a longsword, or (c) any simple weapon
* (a) a diplomat's pack or (b) an entertainer's pack
* (a) a lute or (b) any other musical instrument
* Leather armor and a dagger

```
    npc.addequipment(Equipment.armor['light']['Leather armor'])
    npc.addequipment(Equipment.weapons['all']['Dagger'])

    (_, eq) = choose("Choose equipment: ", 
        { "Longsword": Equipment.weapons['all']['Longsword'], "Rapier" : Equipment.weapons['all']['Rapier'] } | Equipment.weapons['simple'])
    npc.addequipment(eq)

    npc.equipment.append(choose("Choose equipment: ", ["Diplomat's pack", "Entertainer's pack"]) )

    npc.equipment.append(choose("Choose equipment: ", ["Lute", "(musical instrument)"]) )
```

## Spellcasting
*1st-level bard feature*

You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.

### Cantrips
You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table.

### Spell Slots
The Bard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. For example, if you know the 1st-level spell Cure Wounds and have a 1st-level and a 2nd-level spell slot available, you can cast Cure Wounds using either slot.

### Spells Known of 1st Level and Higher
You know four 1st-level spells of your choice from the Bard spell list.

The Spells Known column of the Bard table shows when you learn more bard spells of your choice. Each of these spells must be of a level for which you have spell slots, as shown on the table. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the bard spells you know and replace it with another spell from the bard spell list, which also must be of a level for which you have spell slots.

### Spellcasting Ability
Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier

**Spell attack modifier** = your proficiency bonus + your Charisma modifier

### Ritual Casting
You can cast any bard spell you know as a ritual if that spell has the ritual tag.

### Spellcasting Focus
You can use a musical instrument as a spellcasting focus for your bard spells.

### Spell Versatility
Whenever you finish a long rest, you can replace one spell you learned from this Spellcasting feature with another spell from the bard spell list. The new spell must be the same level as the spell you replace.

```
    bardiccantrips = { 
        1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4,
        11: 4, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4
    }
    bardicspells = {
        1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 14,
        11: 15, 12: 15, 13: 16, 14: 18, 15: 19, 16: 19, 17: 20, 18: 22, 19: 22, 20: 22,
    }
    spellcasting = FullSpellcasting("Bard", "CHA", bardiccantrips, bardicspells)
    npc.append(spellcasting)
```

## Bardic Inspiration
*1st-level bard feature*

You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one [Bardic Inspiration](#bardic-inspiration) die, a d6.

Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the [Bardic Inspiration](#bardic-inspiration) die, but must decide before the DM says whether the roll succeeds or fails. Once the [Bardic Inspiration](#bardic-inspiration) die is rolled, it is lost. A creature can have only one [Bardic Inspiration](#bardic-inspiration) die at a time.

If a creature has a [Bardic Inspiration](#bardic-inspiration) die from you and casts a spell, the creature can roll that die and add the number rolled to one damage or healing roll of the spell. The [Bardic Inspiration](#bardic-inspiration) die is then lost.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.

Your [Bardic Inspiration](#bardic-inspiration) die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.

```
    npc.append(BardicInspiration())
    npc.append(BonusAction("Bardic Inspiration: Inspiration", "Choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die (d{self.npc.bardicinspirationdie})." ))

class BardicInspiration(Feature):
    def __init__(self):
        Feature.__init__(self,"Bardic Inspiration", "You can inspire others through stirring words or music.", "long rest")

    def apply(self):
        npclevels = self.npc.levels("Bard")

        self.uses = self.npc.CHAbonus()
        if self.uses < 1: self.uses = 1

        if npclevels >= 5: self.recharges = "short rest"
        
        self.diesize = 0
        if npclevels < 5: self.diesize = 6
        elif npclevels < 10: self.diesize = 8
        elif npclevels < 15: self.diesize = 10
        else: self.diesize = 12
        self.npc.bardicinspirationdie = self.diesize
```

## Magical Inspiration
*2nd-level bard feature*

If a creature has a [Bardic Inspiration](#bardic-inspiration) die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The [Bardic Inspiration](#bardic-inspiration) die is then lost.

```
def level2(npc):
    npc.append(Feature("Magical Inspiration", "If a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die (a d{self.npc.bardicinspirationdie}) and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost.") )
```

## Jack of All Trades
*2nd-level bard feature*

You can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus.

```
    npc.append(Feature("Jack of All Trades", "You can add {npc.proficiencybonus() // 2} to any ability check you make that doesn't already include your proficiency bonus.") )
```

## Song of Rest
*2nd-level bard feature*

You can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.

```
    npc.append(Feature("Song of Rest", "If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.") )
```

## Bard College
*3rd-level bard feature*

You delve into the advanced techniques of a [bard college](#bard-college) of your choice:

* [Lore](Lore.md)
* [Valor](Valor.md)

Your choice grants you features at 3rd level and again at 6th and 14th level.

```
def level3(npc):
    npc.addsubclass(choose("Choose a Bardic College:", childmods))
```

## Expertise
*3rd-level bard feature*

Choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.

At 10th level, you can choose another two skill proficiencies to gain this benefit.

```
    print(npc.getskills(False))
    chooseexpertise(npc, npc.getskills(False))
    chooseexpertise(npc, npc.getskills(False))
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

## Bardic Versatility
Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing a change in focus as you use your (#ability-score-improvement)skills and magic:

* Replace one of the skills you chose for the [Expertise](#expertise) feature with one of your other skill proficiencies that isn't benefiting from [Expertise](#expertise).
* Replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the bard spell list.

## Font of Inspiration
*5th-level bard feature*

Beginning when you reach 5th level, you regain all of your expended uses of [Bardic Inspiration](#bardic-inspiration) when you finish a short or long rest.

## Countercharm
*6th-level bard feature*

You gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).

```
def level6(npc):
    npc.append(Action("Countercharm", "You can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).") )
```

## Magical Secrets
*10th-level bard feature*

You have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.

The chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.

You learn two additional spells from any class at 14th level and again at 18th level.

```
def level10(npc):
    npc.append(Feature("Magical Secrets", "You have plundered magical knowledge from a wide spectrum of disciplines. Two of your known spells at 10th level, two more at 14th level, and two more at 18th level can be from any classes, including this one.") )

    chooseexpertise(npc, npc.getskills(False))
    chooseexpertise(npc, npc.getskills(False))
```

## Superior Inspiration
At 20th level, when you roll initiative and have no uses of [Bardic Inspiration](#bardic-inspiration) left, you regain one use.

```
def level20(npc):
    npc.append(Feature("Superior Inspiration", "When you roll initiative and have no uses of Bardic Inspiration left, you regain one use.") )
```
