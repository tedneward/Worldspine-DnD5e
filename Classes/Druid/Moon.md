# Druidic Circle: Circle of the Moon
Druids of the Circle of the Moon are fierce guardians of the wilds. Their order gathers under the full moon to share news and trade warnings. They haunt the deepest parts of the wilderness, where they might go for weeks on end before crossing paths with another humanoid creature, let alone another druid.

Changeable as the moon, a druid of this circle might prowl as a great cat one night, soar over the treetops as an eagle the next day, and crash through the undergrowth in bear form to drive off a trespassing monster. The wild is in the druid's blood.

```
name = 'Circle of the Moon'
description = "***Druidic Circle: Circle of the Moon.*** Druids of the Circle of the Moon are fierce guardians of the wilds. Their order gathers under the full moon to share news and trade warnings. They haunt the deepest parts of the wilderness, where they might go for weeks on end before crossing paths with another humanoid creature, let alone another druid. Changeable as the moon, a druid of this circle might prowl as a great cat one night, soar over the treetops as an eagle the next day, and crash through the undergrowth in bear form to drive off a trespassing monster. The wild is in the druid's blood."
```

```
class MoonWildShape(BonusAction):
    def __init__(self):
        BonusAction.__init__(self, "Wild Shape", "", "short rest", "2")

    def evaltext(self): return ""

    def apply(self):
        npclevels = self.npc.levels("Druid")

        beastcr = "1"
        if npclevels >= 6: 
            beastcr = str(npclevels // 3)

        beastmove = ""
        if npclevels < 4: 
            beastmove = "that has no flying or swimming speed"
        elif npclevels < 8: 
            beastmove = "that has no flying speed"

        self.text = f"You can magically assume the shape of a beast that you have seen before. You can transform into any beast that has a challenge rating of {beastcr} or lower{beastmove}. You can stay in a beast shape for {npclevels // 2} hours. You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.\n"

        self.text += """
* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.

* When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.

* You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.

* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.

* You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.
        """    
```

## Combat Wild Shape
*2nd-level Circle of the Moon feature*

You gain the ability to use Wild Shape on your turn as a bonus action, rather than as an action.

Additionally, while you are transformed by Wild Shape, you can use a bonus action to expend one spell slot to regain 1d8 hit points per level of the spell slot expended.

```
def level2(npc):
    npc.remove("Wild Shape")
    npc.append(MoonWildShape())
    npc.append(BonusAction("Combat Wild Shape Healing", "While you are transformed by Wild Shape, you expend one spell slot to regain 1d8 hit points per level of the spell slot expended."))
```

## Circle Forms
*2nd-level Circle of the Moon feature*

The rites of your circle grant you the ability to transform into more dangerous animal forms. You can use your Wild Shape to transform into a beast with a challenge rating as high as 1. You ignore the Max. CR column of the Beast Shapes table, but must abide by the other limitations there.

Starting at 6th level, you can transform into a beast with a challenge rating as high as your druid level divided by 3, rounded down.

## Primal Strike
*6th-level Circle of the Moon feature*

Your attacks in beast form count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.

```
```

## Elemental Wild Shape
*10th-level Circle of the Moon feature*

You can expend two uses of Wild Shape at the same time to transform into an air elemental, an earth elemental, a fire elemental, or a water elemental.

```
```

## Thousand Forms
*14th-level Circle of the Moon feature*

You have learned to use magic to alter your physical form in more subtle ways. You can cast the [alter self](../../Magic/Spells/alter-self.md) spell at will.

```
```