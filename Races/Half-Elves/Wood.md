# Subrace: Wood Elf
One of your parents was a Wood Elf.

***Elf Weapon Training.*** You have proficiency with the longsword, shortsword, shortbow, and longbow.

***Fleet of Foot.*** Your base walking speed increases to 35 feet.

***Mask of the Wild.*** You can attempt to Hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.

```
name = 'Wood'
description = "***Elvish Heritage: Wood Elf.*** One of your parents was a Wood Elf."
def apply(npc):
  npc.addproficiency("Longsword")
  npc.addproficiency("Shortsword")
  npc.addproficiency("Longbow")
  npc.addproficiency("Shortbow")

  npc.speed['walking'] = 35

  npc.append(Feature("Mask of the Wild", "You can attempt to Hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.") )
```
