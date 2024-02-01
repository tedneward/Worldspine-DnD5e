## Mage Slayer
You have practiced techniques in melee combat against spellcasters, gaining the following benefits.

* When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature.
* When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.
* You have advantage on saving throws against spells cast by creatures within 5 feet of you.

```
name = 'Mage Slayer'
description = "***Feat: Mage Slayer.*** You have practiced techniques in melee combat against spellcasters."
def prereq(npc): return True
def apply(npc):
    npc.append(Reaction("Mage Slayer", "When a creature within 5 feet of you casts a spell, you make a melee weapon attack against that creature.") )
    npc.append(Action("Mage Slayer", "When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.") )
    npc.append(Feature("Mage Slayer", "You have advantage on saving throws against spells cast by creatures within 5 feet of you.") )
```
