# Red Dragonborn
Red dragonborn....

### Breath Weapon
You can use your action to exhale destructive flame. It deals damage in a 15' cone. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 fire damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to fire.

### Chromatic Warding
*5th-level Red Dragonborn feature*

As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to fire damage. Once you use this trait, you can't do so again until you finish a long rest.

```
name = 'Red'
description = "***Red Dragonborn.***"
def apply(npc):
    npc.damageresistances.append("fire")
    npc.append(parent.breathweaponaction("15' cone", "fire", "DEX"))
def level5(npc):
    npc.append(Action("Chromatic Warding", "For 1 minute, you become immune to fire damage.", "long rest"))
```
