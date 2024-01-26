# Blue Dragonborn
Blue dragonborn....

### Breath Weapon
You can use your action to exhale destructive lightning. It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to lightning damage.

### Chromatic Warding
*5th-level Blue Dragonborn feature*

As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to lightning damage. Once you use this trait, you can’t do so again until you finish a long rest.

```
name = 'Blue'
description = "***Blue Dragonborn.***"
def apply(npc):
    npc.damageresistances.append("lightning")
    npc.append(parent.breathweaponaction("line 5' x 30'", "lightning", "DEX"))
def level5(npc):
    npc.append(Action("Chromatic Warding", "For 1 minute, you become immune to lightning damage.", "long rest"))
```
