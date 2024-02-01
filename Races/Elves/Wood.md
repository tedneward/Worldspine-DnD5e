# Wood Elf
...

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Elf Weapon Training**. You have proficiency with the longsword, shortsword, shortbow, and longbow.

* **Fleet of Foot**. Your base walking speed increases to 35 feet.

* **Mask of the Wild**. You can attempt to Hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.

```
name = 'Wood'
description = "***Subrace: Wood Elf.***"
def apply(npc):
  npc.WIS += 1

  npc.addproficiency("Longsword")
  npc.addproficiency("Shortsword")
  npc.addproficiency("Longbow")
  npc.addproficiency("Shortbow")

  npc.speed['walking'] = 35

  npc.append(Feature("Mask of the Wild", "You can attempt to Hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.") )
```
