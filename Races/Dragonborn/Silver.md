# Silver Dragonborn
Silver dragonborn....

### Breath Weapon
You can use your action to exhale destructive cold. It deals damage in a 15' cone. When you use your breath weapon, all creatures in the area must make a CON saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to cold.

### Metallic Breath Weapon. 
*5th-level Silver Dragonborn feature*

You gain a second breath weapon. When you take the Attack action on your turn, you can replace one of your attacks with an exhalation in a 15-foot cone. The save DC for this breath is 8 + your Constitution modifier + your proficiency bonus. Whenever you use this trait, choose one:

* Enervating Breath. Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn.
* Repulsion Breath. Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone.
  
Once you use your Metallic Breath Weapon, you can't do so again until you finish a long rest.

```
name = 'Silver'
description = "***Silver Dragonborn.***"
def apply(npc):
    npc.damageresistances.append("cold")
    npc.append(parent.breathweaponaction("15' cone", "cold", "CON"))
def level5(npc):
    npc.append(parent.metallicbreathweaponaction())
```
