# Cleric
Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic.

## Healers and Warriors
Divine magic, as the name suggests, is the power of the gods, flowing from them into the world. Clerics are conduits for that power, manifesting it as miraculous effects. The gods don’t grant this power to everyone who seeks it, but only to those chosen to fulfill a high calling.

Harnessing divine magic doesn’t rely on study or training. A cleric might learn formulaic prayers and ancient rites, but the ability to cast cleric spells relies on devotion and an intuitive sense of a deity’s wishes.

Clerics combine the helpful magic of healing and inspiring their allies with spells that harm and hinder foes. They can provoke awe and dread, lay curses of plague or poison, and even call down flames from heaven to consume their enemies. For those evildoers who will benefit most from a mace to the head, clerics depend on their combat training to let them wade into melee with the power of the gods on their side.

## Divine Agents
Not every acolyte or officiant at a temple or shrine is a cleric. Some priests are called to a simple life of temple service, carrying out their gods’ will through prayer and sacrifice, not by magic and strength of arms. In some cities, priesthood amounts to a political office, viewed as a stepping stone to higher positions of authority and involving no communion with a god at all. True clerics are rare in most hierarchies.

When a cleric takes up an adventuring life, it is usually because his or her god demands it. Pursuing the goals of the gods often involves braving dangers beyond the walls of civilization, smiting evil or seeking holy relics in ancient tombs. Many clerics are also expected to protect their deities’ worshipers, which can mean fighting rampaging orcs, negotiating peace between warring nations, or sealing a portal that would allow a demon prince to enter the world.

Most adventuring clerics maintain some connection to established temples and orders of their faiths. A temple might ask for a cleric’s aid, or a high priest might be in a position to demand it.

```
name = 'Cleric'
description = "***Class: Cleric.*** Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic."
```

## Class features
As a cleric, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|3|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Divine Domain](#divine-domain)
2nd  |+2|3|3|-|-|-|-|-|-|-|-|[Channel Divinity](#channel-divinity) (x1), [Divine Domain](#divine-domain) feature
3rd  |+2|3|4|2|-|-|-|-|-|-|-|
4th  |+2|4|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement)
5th  |+3|4|4|3|2|-|-|-|-|-|-|[Destroy Undead](#destroy-undead) (CR 1/2)
6th  |+3|4|4|3|3|-|-|-|-|-|-|[Channel Divinity](#channel-divinity) (x2), [Divine Domain](#divine-domain) feature
7th  |+3|4|4|3|3|1|-|-|-|-|-|
8th  |+3|4|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement), [Destroy Undead](#destroy-undead) (CR 1), [Divine Domain](#divine-domain) feature
9th  |+4|4|4|3|3|3|1|-|-|-|-|
10th |+4|5|4|3|3|3|2|-|-|-|-|[Divine Intervention](#divine-intervention)
11th |+4|5|4|3|3|3|2|1|-|-|-|[Destroy Undead](#destroy-undead) (CR 2)
12th |+4|5|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement)
13th |+5|5|4|3|3|3|2|1|1|-|-|
14th |+5|5|4|3|3|3|2|1|1|-|-|[Destroy Undead](#destroy-undead) (CR 3)
15th |+5|5|4|3|3|3|2|1|1|1|-|
16th |+5|5|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement)
17th |+6|5|4|3|3|3|2|1|1|1|1|[Destroy Undead](#destroy-undead) (CR 4), [Divine Domain](#divine-domain) feature
18th |+6|5|4|3|3|3|3|1|1|1|1|[Channel Divinity](#channel-divinity) (x3)
19th |+6|5|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement)
20th |+6|5|4|3|3|3|3|2|2|1|1|[Divine Intervention](#divine-intervention) improvement

```
cantriptable = {
    1: 3, 2: 3, 3: 3, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 5,
    11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 5, 17: 5, 18: 5, 19: 5, 20: 5
}
```


### Hit Points
**Hit Dice**: 1d8 per cleric level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per cleric level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor, medium armor, shields

**Weapons**: All simple weapons

**Tools**: None

**Saving Throws**: Wisdom, Charisma

**Skills**: Choose two from History, Insight, Medicine, Persuasion, and Religion

```
def level1(npc):
    for arm in Equipment.armor['light'] | Equipment.armor['medium'] | Equipment.armor['shields']:
        npc.addproficiency(arm)
    for wpn in Equipment.weapons['simple']:
        npc.addproficiency(wpn)

    npc.addproficiency('WIS')
    npc.addproficiency('CHA')

    skillchoices = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
    chooseskill(npc, skillchoices)
    chooseskill(npc, skillchoices)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a mace or (b) a warhammer (if proficient)
* (a) scale mail, (b) leather armor, or (c) chain mail (if proficient)
* (a) a light crossbow and 20 bolts or (b) any simple weapon
* (a) a priest's pack or (b) an explorer's pack
* A shield and a holy symbol

```
    if "Warhammer" in npc.getproficiencies():
        aorb = choose("Choose equipment: ", ["Mace", "Warhammer"])
        npc.addequipment(Equipment.weapons['all'][aorb])
    else:
        npc.addequipment(Equipment.weapons['all']['Mace'])

    armoroptions = ["Scale mail", "Leather armor"]
    if "Chain mail" in npc.getproficiencies():
        armoroptions.append("Chain mail")
    armorchoice = choose("Choose equipment: ", armoroptions)
    npc.addequipment(Equipment.armor['all'][armorchoice])

    aorb = choose("Choose equipment: ", ["Light crossbow", "Any simple weapon"])
    if aorb == "Light crossbow":
        npc.addequipment(Equipment.weapons['all']["Light crossbow"])
    else:
        (_, eq) = choose("Choose equipment: ", Equipment.weapons['simple'])
        npc.addequipment(eq)

    aorb = choose("Choose equipment: ", ["Priest's pack", "Explorer's pack"])
    npc.addequipment(aorb)
    npc.addequipment(Equipment.armor['all']['Shield'])
    npc.addequipment("Holy symbol")
```

## Spellcasting
*1st-level cleric feature*

As a conduit for divine power, you can cast cleric spells.

### Cantrips
At 1st level, you know three cantrips of your choice from the cleric spell list. You learn additional cleric cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Cleric table.

### Preparing and Casting Spells
The Cleric table shows how many spell slots you have to cast your cleric spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell’s level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list. When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you are a 3rd-level cleric, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell cure wounds, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn’t remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of cleric spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.

### Spellcasting Ability
Wisdom is your spellcasting ability for your cleric spells. The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

### Ritual Casting
You can cast a cleric spell as a ritual if that spell has the *ritual* tag and you have the spell prepared.

### Spellcasting Focus
You can use a holy symbol as a spellcasting focus for your cleric spells.


```
    spellcasting = DivineSpellcasting("Cleric", cantriptable)
    npc.append(spellcasting)
```


## Divine Domain
*1st-level cleric feature*

Choose one domain, or choose a [diety or religion](../../Religions/index.md) and select one of their domains:

* [Life](Life.md)

Your choice grants you domain spells and other features when you choose it at 1st level. It also grants you additional ways to use [Channel Divinity](#channel-divinity) when you gain that feature at 2nd level, and additional benefits at 6th, 8th, and 17th levels.

```
    domainmod = choose("Choose a Divine Domain:", childmods)
    npc.addsubclass(domainmod)

    # Bring domain spells into Spellcasting
    if getattr(domainmod, "domainspells", None) != None:
        spellcasting.addspellspreparedtable(domainmod.domainspells)
```

## Domain Spells
*1st-level cleric feature*

Each domain has a list of spells--its domain spells that you gain at the cleric levels noted in the domain description. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day.

If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

## Channel Divinity
*2nd-level cleric feature*

You gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with three such effects: Turn Undead, Harness Divine Power, and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.

When you use your [Channel Divinity](#channel-divinity), you choose which effect to create. You must then finish a short or long rest to use your [Channel Divinity](#channel-divinity) again.

Some [Channel Divinity](#channel-divinity) effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.

Beginning at 6th level, you can use your [Channel Divinity](#channel-divinity) twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses.

```
class ChannelDivinity(Feature):
    def __init__(self):
        Feature.__init__(self, "Channel Divinity", "See below for details on each use of your Channel Divinity feature.", "short rest")

    def apply(self):
        npclevels = self.npc.levels("Cleric")
        if npclevels < 18: self.uses = 2
        else: self.uses = 3

        self.text += " Creatures that must save against any of your Channel Divinity features do so at DC " + self.savedc()

    def savedc(self):
        return 8 + self.npc.proficiencybonus() + self.npc.WISbonus()

def level2(npc):
    npc.append(ChannelDivinity())
```

## Channel Divinity: Turn Undead
*2nd-level cleric feature*

As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

```
    npc.append(Action("Channel Divinity: Turn Undead", "You can use one of your uses of Channel Divinity to turn undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.") )
```

## Channel Divinity: Harness Divine Power
*2nd-level cleric feature*

You can expend a use of your [Channel Divinity](#channel-divinity) to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 2nd level, once; 6th level, twice; and 18th level, thrice. You regain all expended uses when you finish a long rest.

```
    npc.append(BonusAction("Channel Divinity: Harness Divine Power", "You can expend a use of your Channel Divinity to regain one expended spell slot, the level of which can be no higher than {(npc.proficiencybonus() // 2) + 1}.") )
```

## [Ability Score Improvement](#ability-score-improvement)
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): choosefeatorasi(npc)
def level8(npc): choosefeatorasi(npc)
def level12(npc): choosefeatorasi(npc)
def level16(npc): choosefeatorasi(npc)
def level19(npc): choosefeatorasi(npc)
```

## Cantrip Versatility
*4th-level cleric feature*

Whenever you reach a level in this class that grants the [Ability Score Improvement](#ability-score-improvement) feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the cleric spell list. 

## Destroy Undead
*5th-level cleric feature*

When an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown below:

**Destroy Undead Table**

Cleric Level | Destroys Undead of CR ...
-------------|--------------------------
5th | 1/2 or lower
8th | 1 or lower
11th| 2 or lower
14th| 3 or lower
17th| 4 or lower

```
def level5(npc):
    npc.replace("Channel Divinity: Turn Undead", Action("Channel Divinity: Turn Undead", "You can use one of your uses of Channel Divinity to turn undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, if it is a CR of {'1/2' if npc.levels('Cleric') < 8 else '1' if npc.levels('Cleric') < 11 else '2' if npc.levels('Cleric') < 14 else '3' if npc.levels('Cleric') < 17 else '4'} or lower it is destroyed; otherwise it is turned for 1 minute or until it takes any damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.") )
```

## Divine Intervention
*10th-level cleric feature*

You can call on your deity to intervene on your behalf when your need is great.

Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.

At 20th level, your call for intervention succeeds automatically, no roll required.

```
def level10(npc):
    npc.append(Action("Divine Intervention", "Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.", "long rest or 7 days") )

def level20(npc):
    npc.replace("Divine Intervention", Action("Divine Intervention", "Describe the assistance you seek, and your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. Afterwards, you can't use this feature again for 7 days.", "7 days") )
```
