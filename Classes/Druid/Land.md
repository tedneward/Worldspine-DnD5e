# Druidic Circle: Circle of the Land
The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle’s wisest members preside as the chief priests of communities that hold to the Old Faith and serve as advisors to the rulers of those folk. As a member of this circle, your magic is influenced by the land where you were initiated into the circle’s mysterious rites.

```
name = 'Circle of the Land'
description = "***Druidic Circle: Circle of the Land.*** The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle’s wisest members preside as the chief priests of communities that hold to the Old Faith and serve as advisors to the rulers of those folk. As a member of this circle, your magic is influenced by the land where you were initiated into the circle’s mysterious rites."
```

## Bonus Cantrip
*2nd-level Circle of the Land feature*

You learn one additional druid cantrip of your choice.

```
def level2(npc):
    npc.find("Druid Spellcasting").maxcantripsknown += 1
```

## Natural Recovery
*2nd-level Circle of the Land feature*

You can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest.

For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.

```
    npc.append(Feature("Natural Recovery","During a short rest, you can recover up to {(npc.levels('Druid') + 1) // 2} total spell slots of less than 6th level.", "long rest") )
```

## Circle Spells
Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Choose that land – arctic, coast, desert, forest, grassland, mountain, swamp, or Underdark – and consult the associated list of spells.

Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.

```
    choices = {
        'Arctic' : arcticcirclespells, 
        'Coast' : coastcirclespells, 
        'Desert' : desertcirclespells, 
        'Forest' : forestcirclespells, 
        'Grassland' : grasslandcirclespells, 
        'Mountain' : mountaincirclespells, 
        'Swamp' : swampcirclespells, 
        'Underdark' : underdarkcirclespells
    }
    (land, circlespells) = choose("Choose your Land: ", choices)
    npc.find("Druid Spellcasting").addspellspreparedtable(circlespells)
    npc.description.append("***Circle of the Land: " + land + ".***")
```

**Arctic**

Druid Level| Circle Spells
---------- | --------------
3rd	| [hold person](../../Magic/Spells/hold-person.md), [spike growth](../../Magic/Spells/spike-growth.md)
5th	| [sleet storm](../../Magic/Spells/sleet-storm.md), [slow](../../Magic/Spells/slow.md)
7th	| [freedom of movement](../../Magic/Spells/freedom-of-movement.md), [ice storm](../../Magic/Spells/ice-storm.md)
9th	| [commune with nature](../../Magic/Spells/commune-with-nature.md), [cone of cold](../../Magic/Spells/cone-of-cold.md)

```
arcticcirclespells = {
    3: ['hold person', 'spike growth'],
    5: ['slow', 'sleet storm'],
    7: ['freedom of movement', 'ice storm'],
    9: ['commune with nature', 'cone of cold']
}
```

**Coast**

Druid Level| Circle Spells
---------- | --------------
3rd	| [mirror image](../../Magic/Spells/mirror-image.md), [misty step](../../Magic/Spells/misty-step.md)
5th	| [water breathing](../../Magic/Spells/water-breathing.md), [water walk](../../Magic/Spells/water-walk.md)
7th	| [control water](../../Magic/Spells/control-water.md), [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
9th	| [conjure elemental](../../Magic/Spells/conjure-elemental.md), [scrying](../../Magic/Spells/scrying.md)

```
coastcirclespells = {
    3: ['mirror image', 'misty step'],
    5: ['water breathing', 'water walk'],
    7: ['freedom of movement', 'control water'],
    9: ['conjure elemental', 'scrying']
}
```

**Desert**

Druid Level| Circle Spells
---------- | --------------
3rd | [blur](../../Magic/Spells/blur.md), [silence](../../Magic/Spells/silence.md)
5th | [create food and water](../../Magic/Spells/create-food-and-water.md), [protection from energy](../../Magic/Spells/protection-from-energy.md)
7th | [blight](../../Magic/Spells/blight.md), [hallucinatory terrain](../../Magic/Spells/hallucinatory-terrain.md)
9th | [insect plague](../../Magic/Spells/insect-plague.md), [wall of stone](../../Magic/Spells/wall-of-stone.md)

```
desertcirclespells = {
    3: ['blur', 'silence'],
    5: ['create food and water', 'protection from energy'],
    7: ['blight', 'hallucinatory terrain'],
    9: ['insect plague', 'wall of stone']
}
```

**Forest**

Druid Level| Circle Spells
---------- | --------------
3rd	| barkskin, spider climb
5th	| call lightning, plant growth
7th	| divination, freedom of movement
9th	| commune with nature, tree stride

```
forestcirclespells = {
    3: ['barkskin', 'spider climb'],
    5: ['call lightning', 'plant growth'],
    7: ['divination', 'freedom of movement'],
    9: ['commune with nature', 'tree stride']
}
```

**Grassland**

Druid Level| Circle Spells
---------- | --------------
3rd	| Invisibility, Pass Without Trace
5th	| Daylight, Haste
7th	| Divination, Freedom of Movement
9th	| Dream, Insect Plague

```
grasslandcirclespells = {
    3: ['invisibility', 'pass without trace'],
    5: ['daylight', 'haste'],
    7: ['divination', 'freedom of movement'],
    9: ['dream', 'insect plague']
}
```

**Mountain**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Spider Climb, Spike Growth
5th	|Lightning Bolt, Meld into Stone
7th	|Stone Shape, Stoneskin
9th	|Passwall, Wall of Stone

```
mountaincirclespells = {
    3: ['spider climb', 'spike growth'],
    5: ['lightning bolt', 'meld into stone'],
    7: ['stone shape', 'stoneskin'],
    9: ['passwall', 'wall of stone']
}
```

**Swamp**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Darkness, Melf's Acid Arrow
5th	|Water Walk, Stinking Cloud
7th	|Freedom of Movement, Locate Creature
9th	|Insect Plague, Scrying

```
swampcirclespells = {
    3: ['darkness', "melf's acid arrow"],
    5: ['water walk', 'stinking cloud'],
    7: ['freedom of movement', 'locate creature'],
    9: ['insect plague', 'scrying']
}
```

**Underdark**

Druid Level| Circle Spells
---------- | --------------
3rd	|Spider Climb, Web
5th	|Gaseous Form, Stinking Cloud
7th	|Greater Invisibility, Stone Shape
9th	|Cloudkill, Insect Plague

```
underdarkcirclespells = {
    3: ['spider climb', 'web'],
    5: ['gaseous form', 'stinking cloud'],
    7: ['greater invisibility', 'stone shape'],
    9: ['cloudkill', 'insect plague']
}
```



## Land's Stride
*6th-level Circle of the Land feature*

Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.

In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.

```
def level6(npc):
    npc.append(Feature("Land's Stride", "Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.") )
```

## Nature's Ward
*10th-level Circle of the Land feature*

You can't be charmed or frightened by elementals or fey, and you are immune to poison and disease.

```
def level10(npc):
    npc.append(Feature("Nature's Ward", "You can't be charmed or frightened by elementals or fey."))
    npc.damageimmunities.append('poison')
    npc.conditionimmunities.append('poisoned')
    npc.conditionimmunities.append('diseased')
```

## Nature's Sanctuary
*14th-level Circle of the Land feature*

Creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours.

The creature is aware of this effect before it makes its attack against you.

```
def level14(npc):
    npc.append(Feature("Nature's Sanctuary", "Creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw (DC {self.npc.find('Druid Spellcasting').spellsavedc()}). On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours. The creature is aware of this effect before it makes its attack against you."))
```
