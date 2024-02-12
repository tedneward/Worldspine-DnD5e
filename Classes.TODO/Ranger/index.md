# Ranger
Far from the bustle of cities and towns, past the hedges that shelter the most distant farms from the terrors of the wild, amid the dense-packed trees of trackless forests and across wide and empty plains, rangers keep their unending watch.

## Deadly Hunters
Warriors of the wilderness, rangers specialize in hunting the monsters that threaten the edges of civilization — humanoid raiders, rampaging beasts and monstrosities, terrible giants, and deadly dragons. They learn to track their quarry as a predator does, moving stealthily through the wilds and hiding themselves in brush and rubble. Rangers focus their combat training on techniques that are particularly useful against their specific favored foes.

Thanks to their familiarity with the wilds, rangers acquire the ability to cast spells that harness nature’s power, much as a druid does. Their spells, like their combat abilities, emphasize speed, stealth, and the hunt. A ranger’s talents and abilities are honed with deadly focus on the grim task of protecting the borderlands.

## Independent Adventurers
Though a ranger might make a living as a hunter, a guide, or a tracker, a ranger’s true calling is to defend the outskirts of civilization from the ravages of monsters and humanoid hordes that press in from the wild. In some places, rangers gather in secretive orders or join forces with druidic circles. Many rangers, though, are independent almost to a fault, knowing that, when a dragon or a band of orcs attacks, a ranger might be the first — and possibly the last — line of defense.

This fierce independence makes rangers well suited to adventuring, since they are accustomed to life far from the comforts of a dry bed and a hot bath. Faced with city-bred adventurers who grouse and whine about the hardships of the wild, rangers respond with some mixture of amusement, frustration, and compassion. But they quickly learn that other adventurers who can carry their own weight in a fight against civilization’s foes are worth any extra burden. Coddled city folk might not know how to feed themselves or find fresh water in the wild, but they make up for it in other ways.

*You must have a Dexterity score and a Wisdom score of 13 or higher in order to multiclass in or out of this class.*

```
name = 'Ranger'
description = "***Class: Ranger.*** Far from the bustle of cities and towns, past the hedges that shelter the most distant farms from the terrors of the wild, amid the dense-packed trees of trackless forests and across wide and empty plains, rangers keep their unending watch."
```

Level|Proficiency Bonus|Spells Known|1st|2nd|3rd|4th|5th|Features
-----|-----------------|------------|---|---|---|---|---|--------
1st  |+2 | - |-|-|-|-|-|[Favored Foe](#favored-foe), [Deft Explorer](#deft-explorer)
2nd  |+2 | 2 |2|-|-|-|-|[Fighting Style](#fighting-style), [Spellcasting](#spellcasting)
3rd  |+2 | 3 |3|-|-|-|-|[Primeval Awareness](#primeval-awareness), [Ranger Conclave](#ranger-conclave)
4th  |+2 | 3 |3|-|-|-|-|Ability Score Improvement
5th  |+3 | 4 |4|2|-|-|-|Ranger Conclave feature
6th  |+3 | 4 |4|2|-|-|-|[Greater Favored Enemy](#greater-favored-enemy)
7th  |+3 | 5 |4|3|-|-|-|Ranger Conclave feature
8th  |+3 | 5 |4|3|-|-|-|Ability Score Improvement, [Fleet of Foot](#fleet-of-foot)
9th  |+4 | 6 |4|3|2|-|-|
10th |+4 | 6 |4|3|2|-|-|[Nature's Veil](#natures-veil)
11th |+4 | 7 |4|3|3|-|-|Ranger Conclave feature
12th |+4 | 7 |4|3|3|-|-|Ability Score Improvement
13th |+5 | 8 |4|3|3|1|-|
14th |+5 | 8 |4|3|3|1|-|[Vanish](#vanish)
15th |+5 | 9 |4|3|3|2|-|Ranger Conclave feature
16th |+5 | 9 |4|3|3|2|-|Ability Score Improvement
17th |+6 | 10|4|3|3|3|1|
18th |+6 | 10|4|3|3|3|1|[Feral Senses](#feral-senses)
19th |+6 | 11|4|3|3|3|2|Ability Score Improvement
20th |+6 | 11|4|3|3|3|2|[Foe Slayer](#foe-slayer)

```
spellsknowntable = {
    1: 0, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 5, 8: 5, 9: 6, 10: 6,
    11: 7, 12: 7, 13: 8, 14: 8, 15: 9, 16: 9, 17: 10, 18:10, 19: 11, 20: 11,
}
```

As a ranger, you gain the following class features.

## Hit Points
**Hit Dice**: 1d10 per ranger level

**Hit Points at 1st Level**: 10 + your Constitution modifier

**Hit Points at Higher Levels**: 1d10 (or 6) + your Constitution modifier per ranger level after 1st

```
def everylevel(npc): npc.hits('d10')
```

## Proficiencies
**Armor**: Light armor, medium armor, shields

**Weapons**: Simple weapons, martial weapons

**Tools**: None

**Saving Throws**: Strength, Dexterity

**Skills**: Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival

```
def level1(npc):
    for arm in Equipment.armor['light'] + Equipment.armor['medium'] + Equipment.armor['shields']:
        npc.addproficiency(arm)
    for wpn in Equipment.weapons['simple'] + Equipment.weapons['martial']:
        npc.addproficiency(wpn)

    npc.addproficiency('STR')
    npc.addproficiency('DEX')

    chooseskill(npc, ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'])
    chooseskill(npc, ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'])
    chooseskill(npc, ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'])
```

## Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) scale mail or (b) leather armor
* (a) two shortswords or (b) two simple melee weapons
* (a) a dungeoneer's pack or (b) an explorer's pack
* A longbow and a quiver of 20 arrows

```
    # Equipment
```

## Favored Enemy
*1st-level ranger feature*

You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.

Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.

You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.

When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.

You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures.

```
    npc.favoredenemies = []
    favoredenemy = choose("Choose a favored enemy: ", ['Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Fiend', 'Giant', 'Monstrosity', 'Ooze', 'Plant', 'Undead', 'Two humanoid races'])
    if favoredenemy = 'Two humanoid races':
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
    else:
        npc.favoredenemies.append(favoredenemy)

    chooselanguage(npc, 'All')

    class FavoredEnemy(Feature):
        def __init__(self):
            Feature.__init__(self, "Favored Enemy", "")

        def apply(self):
            self.text = f"You have significant experience studying, tracking, hunting, and even talking to certain types of enemies: {",".join(self.npc.favoredenemies)}. You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them."

    npc.append(FavoredEnemy())

def level6(npc):
    favoredenemy = choose("Choose a favored enemy: ", ['Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Fiend', 'Giant', 'Monstrosity', 'Ooze', 'Plant', 'Undead', 'Two humanoid races'])
    if favoredenemy = 'Two humanoid races':
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
    else:
        npc.favoredenemies.append(favoredenemy)

    chooselanguage(npc, 'All')

def level14(npc):
    favoredenemy = choose("Choose a favored enemy: ", ['Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Fiend', 'Giant', 'Monstrosity', 'Ooze', 'Plant', 'Undead', 'Two humanoid races'])
    if favoredenemy = 'Two humanoid races':
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
        npc.favoredenemies.append(choose("Choose a favored enemy: ", ['Goblin', 'Hobgoblin', 'Orc', 'Troll']))
    else:
        npc.favoredenemies.append(favoredenemy)

    chooselanguage(npc, 'All')
```


## Natural Explorer
*1st-level ranger feature*

You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you’re proficient in.

While traveling for an hour or more in your favored terrain, you gain the following benefits:

* Difficult terrain doesn’t slow your group’s travel.
* Your group can’t become lost except by magical means.
* Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.
* If you are traveling alone, you can move stealthily at a normal pace.
* When you forage, you find twice as much food as you normally would.
* While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.

You choose additional favored terrain types at 6th and 10th level.

```

```

## Fighting Style
*2nd-level ranger feature*

You adopt a particular style of fighting as your specialty. Choose one of the [styles available](Fighter/Styles.md). You can't take a Fighting Style option more than once, even if you later get to choose again.

In addition, you have access to the following fighting style:

* **Druidic Warrior**: You learn two cantrips of your choice from the druid spell list. They count as ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the druid spell list.

### Martial Versatility
Whenever you gain a level, you can replace a fighting style you know with another style available to your class. This change represents a shift of focus in your martial training and practice, causing you to lose the benefits of one style and gain the benefits of another style.

```
def druidicwarrior(npc):
    innatecasting = InnateCasting("Druidic Warrior", "WIS")
    availablecantrips = [
        'druidcraft', 'guidance', 'mending', 'poison spray', 
        'produce flame', 'resistance', 'shillelagh'
    ]
    innatecasting.atwill.append(choose("Choose a cantrip:", availablecantrips))
    innatecasting.atwill.append(choose("Choose a cantrip:", availablecantrips))
    npc.append(innatecasting)

def level2(npc):
    styles = findmodule("Fighter").getfightingstyles()
    styles['Druidic Warrior'] = druidicwarrior
    findmodule("Fighter").choosestyle(npc, styles)
```

## Spellcasting
*2nd-level ranger feature*

You have learned to use the magical essence of nature to cast spells, much as a druid does.

### Spell Slots
The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Animal Friendship and have a 1st-level and a 2nd-level spell slot available, you can cast Animal Friendship using either slot.

### Spells Known of 1st Level and Higher
You know two 1st-level spells of your choice from the ranger spell list. The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots.

### Spellcasting Ability
Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

### Spell Versatility
Whenever you finish a long rest, you can replace one spell you learned from this Spellcasting feature with another spell from the ranger spell list. The new spell must be the same level as the spell you replace.

### Spellcasting Focus
You can use a druidic focus as a spellcasting focus for your ranger spells.

```
    rangerspellcasting = HalfSpellcasting("Ranger", "WIS", {}, spellsknowntable)
    npc.append(rangerspellcasting)
```


## Ranger Conclave
*3rd level ranger feature*

You choose to emulate the ideals and training of a ranger conclave:

* [Beast Master](BeastMaster.md)
* [Hunter](Hunter.md)

Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level.

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

## Greater Favored Enemy
*6th-level ranger feature*

You are ready to hunt even deadlier game. Choose a type of greater favored enemy: aberrations, celestials, constructs, dragons, elementals, fiends, or giants. You gain all the benefits against this chosen enemy that you normally gain against your favored enemy, including an additional language. Your bonus to damage rolls against all your favored enemies increases to +4.

Additionally, you have advantage on saving throws against the spells and abilities used by a greater favored enemy.

## Fleet of Foot
*8th-level ranger feature*

You can use the Dash action as a bonus action on your turn.

## Vanish
*14th-level ranger feature*

You can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail.

## Feral Senses
*18th-level ranger feature*

You gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.

You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened.

## Foe Slayer
*20th-level ranger feature*

You become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.

---

# Ranger Spells
The following spells listed are known (but not necessarily accessible, depending on the conclave chosen) to all rangers throughout Azgaarnoth; this is not the complete list of all ranger spells, however. Certain conclaves may have additional spells that are only known to them, and thus are not accessible to other conclaves. Rangers can learn new spells by visiting druidic circles, communing with nature for significant periods of time, studying with another ranger of a different conclave, and so on. (In other words, DMs can release new ranger spells, but all rangers do not have access to them by default.)

Rangers can, at the discretion of the DM, learn spells from other druids or rangers, but generally this requires some exchange, usually a deed done on behalf of the spell's source.

## 1st Level
* [absorb elements](../../Magic/Spells/absorb-elements.md)
* [alarm](../../Magic/Spells/alarm.md)
* [animal friendship](../../Magic/Spells/animal-friendship.md)
* [attract projectiles](../../Magic/Spells/attract-projectiles.md)
* [beast bond](../../Magic/Spells/beast-bond.md)
* [blackout](../../Magic/Spells/blackout.md)
* [cure wounds](../../Magic/Spells/cure-wounds.md)
* [detect magic](../../Magic/Spells/detect-magic.md)
* [detect poison and disease](../../Magic/Spells/detect-poison-and-disease.md)
* [ensnaring strike](../../Magic/Spells/ensnaring-strike.md)
* [entangle](../../Magic/Spells/entangle.md)
* [fog cloud](../../Magic/Spells/fog-cloud.md)
* [glide](../../Magic/Spells/glide.md)
* [goodberry](../../Magic/Spells/goodberry.md)
* [hail of thorns](../../Magic/Spells/hail-of-thorns.md)
* [hunter's mark](../../Magic/Spells/hunters-mark.md)
* [jump](../../Magic/Spells/jump.md)
* [leaf shield](../../Magic/Spells/leaf-shield.md)
* [longstrider](../../Magic/Spells/longstrider.md)
* [searing smite](../../Magic/Spells/searing-smite.md)
* [snare](../../Magic/Spells/snare.md)
* [speak with animals](../../Magic/Spells/speak-with-animals.md)
* [sudden awakening](../../Magic/Spells/sudden-awakening.md)
* [swoop](../../Magic/Spells/swoop.md)
* [wild cunning](../../Magic/Spells/wild-cunning.md)
* [zephyr strike](../../Magic/Spells/zephyr-strike.md)

## 2nd Level
* [aid](../../Magic/Spells/aid.md)
* [animal messenger](../../Magic/Spells/animal-messenger.md)
* [barkskin](../../Magic/Spells/barkskin.md)
* [beast sense](../../Magic/Spells/beast-sense.md)
* [blades of grass](../../Magic/Spells/blades-of-grass.md)
* [cordon of arrows](../../Magic/Spells/cordon-of-arrows.md)
* [darkvision](../../Magic/Spells/darkvision.md)
* [dive](../../Magic/Spells/dive.md)
* [drown](../../Magic/Spells/drown.md)
* [enhance ability](../../Magic/Spells/enhance-ability.md)
* [find traps](../../Magic/Spells/find-traps.md)
* [gust of wind](../../Magic/Spells/gust-of-wind.md)
* [lesser restoration](../../Magic/Spells/lesser-restoration.md)
* [locate animals or plants](../../Magic/Spells/locate-animals-or-plants.md)
* [locate object](../../Magic/Spells/locate-object.md)
* [magic weapon](../../Magic/Spells/magic-weapon.md)
* [pass without trace](../../Magic/Spells/pass-without-trace.md)
* [protection from poison](../../Magic/Spells/protection-from-poison.md)
* [silence](../../Magic/Spells/silence.md)
* [spike growth](../../Magic/Spells/spike-growth.md)
* [summon beast](../../Magic/Spells/summon-beast.md)
* [warding bond](../../Magic/Spells/warding-bond.md)

## 3rd Level
* [blinding smite](../../Magic/Spells/blinding-smite.md)
* [conjure animals](../../Magic/Spells/conjure-animals.md)
* [conjure barrage](../../Magic/Spells/conjure-barrage.md)
* [daylight](../../Magic/Spells/daylight.md)
* [flame arrows](../../Magic/Spells/flame-arrows.md)
* [healing wave](../../Magic/Spells/healing-wave.md)
* [lightning arrow](../../Magic/Spells/lightning-arrow.md)
* [meld into stone](../../Magic/Spells/meld-into-stone.md)
* [nondetection](../../Magic/Spells/nondetection.md)
* [plant growth](../../Magic/Spells/plant-growth.md)
* [protection from energy](../../Magic/Spells/protection-from-energy.md)
* [revivify](../../Magic/Spells/revivify.md)
* [speak with plants](../../Magic/Spells/speak-with-plants.md)
* [tongues](../../Magic/Spells/tongues.md)
* [veiled blade](../../Magic/Spells/veiled-blade.md)
* [water breathing](../../Magic/Spells/water-breathing.md) (ritual)
* [water walk](../../Magic/Spells/water-walk.md) (ritual)
* [wind wall](../../Magic/Spells/wind-wall.md)

## 4th Level
* [conjure woodland beings](../../Magic/Spells/conjure-woodland-beings.md)
* [death ward](../../Magic/Spells/death-ward.md)
* [dominate beast](../../Magic/Spells/dominate-beast.md)
* [enhance body](../../Magic/Spells/enhance-body.md)
* [envenomed weapon](../../Magic/Spells/envenomed-weapon.md)
* [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
* [grasping vine](../../Magic/Spells/grasping-vine.md)
* [greater renewal](../../Magic/Spells/greater-renewal.md)
* [guardian of nature](../../Magic/Spells/guardian-of-nature.md)
* [locate creature](../../Magic/Spells/locate-creature.md)
* [stockade sprouts](../../Magic/Spells/stockade-sprouts.md)
* [stoneskin](../../Magic/Spells/stoneskin.md)
* [wind funnel](../../Magic/Spells/wind-funnel.md)

## 5th Level
* [awaken](../../Magic/Spells/awaken.md)
* [burrow](../../Magic/Spells/burrow.md)
* [commune with nature](../../Magic/Spells/commune-with-nature.md)
* [conjure volley](../../Magic/Spells/conjure-volley.md)
* [greater restoration](../../Magic/Spells/greater-restoration.md)
* [reverse projectiles](../../Magic/Spells/reverse-projectiles.md)
* [soar](../../Magic/Spells/soar.md)
* [swift quiver](../../Magic/Spells/swift-quiver.md)
* [tree stride](../../Magic/Spells/tree-stride.md)
