## Moderately Armored
*Prerequisite: Proficiency with light armor*

You have trained to master the use of medium armor and shields, gaining the following benefits:

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* You gain proficiency with medium armor and shields.

```
name = 'Moderately Armored'
description = "***Feat: Moderately Armored.*** You have trained to master the use of medium armor and shields."
def prereq(npc): 
    for lightarmor in Equipment.armor['light']:
        if lightarmor in npc.proficiencies:
            return True
    return False

def apply(npc):
    abilityscoreincrease(npc, ['STR','DEX'])

    for arm in Equipment.armor['medium'] | Equipment.armor['shields']:
        npc.addproficiency(arm)
```

