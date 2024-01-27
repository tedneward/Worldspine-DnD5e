## Great Weapon Master
You've learned to put the weight of a weapon to your advantage, letting its momentum empower your strikes. You gain the following benefits:

* On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action.
* Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.

```
name = 'Great Weapon Master'
description = "***Feat: Great Weapon Master.*** You've learned to put the weight of a weapon to your advantage, letting its momentum empower your strikes."
def prereq(npc): return True
def apply(npc):
    npc.append(BonusAction("Great Weapon Master", "When you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you make one melee weapon attack.") )
    npc.append(Action("Great Weapon Master", "Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.") )
```
