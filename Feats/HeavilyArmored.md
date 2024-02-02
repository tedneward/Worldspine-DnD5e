## Heavily Armored
*Prerequisite: Proficiency with medium armor*

You have trained to master the use of heavy armor, gaining the following benefits:

* Increase your Strength score by 1, to a maximum of 20.
* You gain proficiency with heavy armor.

```
name = 'Heavily Armored'
description = "***Feat: Heavily Armored.*** You have trained to master the use of heavy armor."
def prereq(npc): 
    for arm in Equipment.armor['medium']:
        if arm in npc.proficiencies:
            return True
    return False
def apply(npc):
    npc.STR += 1

    for arm in Equipment.armor['heavy']:
        npc.addproficiency(arm)
```
