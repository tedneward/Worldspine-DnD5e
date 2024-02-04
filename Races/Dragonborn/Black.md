# Black Dragonborn
Descendant of black dragons, black dragonborn are often moody and reclusive, regardless of alignment.

Black dragonborn tend to be haughty and aloof, even among the more good-minded. They savor cunning, particularly their own, and often use it to gain dominance over their opponents. As hunters, for example, they often relish the chance to outwit their enemies. Some black dragonborn prefer to remain in shadows, unwilling to cause suspicion by leaving evidence of their involvement or existence, because they realize that beasts are not the only predators to be wary of. Black dragonborn of any alignment may pride themselves on having a level head but those willing to test their ire would be making a grave mistake.

### Breath Weapon
You can use your action to exhale destructive acid. It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to acid.

### Chromatic Warding
*5th-level Black Dragonborn feature*

As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to acid damage. Once you use this trait, you can't do so again until you finish a long rest.

```
name = 'Black'
description = "***Black Dragonborn.*** Descendant of black dragons, black dragonborn are often moody and reclusive, regardless of alignment."
def apply(npc):
    npc.damageresistances.append("acid")
    npc.append(parent.breathweaponaction("line 5' x 30'", "acid", "DEX"))
def level5(npc):
    npc.append(Action("Chromatic Warding", "For 1 minute, you become immune to acid damage.", "long rest"))
```
