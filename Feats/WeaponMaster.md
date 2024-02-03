## Weapon Master
You have practiced extensively with a variety of weapons, gaining the following benefits:

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* You gain proficiency with four weapons of your choice. Each one must be a simple or a martial weapon.

```
name = 'Weapon Master'
description = "***Feat: Weapon Master.*** You have practiced extensively with a variety of weapons."
def prereq(npc): return True
def apply(npc):
    abilityscoreincrease(npc, ['STR','DEX'])

    for _ in range(0, 4):
        wpn = choose("Choose a weapon proficiency: ", Equipment.weapons['martial-melee'] | Equipment.weapons['martial-ranged'] | Equipment.weapons['simple-melee'] | Equipment.weapons['simple-ranged'])
        npc.addproficiency(wpn[0])
```
