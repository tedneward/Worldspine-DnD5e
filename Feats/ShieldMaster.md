## Shield Master
You use shields not just for protection but also for offense. You gain the following benefits while you are wielding a shield:

* If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield.
* If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you.
* If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect.

```
name = 'Shield Master'
description = "***Feat: Shield Master.*** You use shields not just for protection but also for offense."
def prereq(npc): return True
def apply(npc):
    npc.append(BonusAction("Shield Bash", "When you take the Attack action on your turn, you can try to Shove a creature within 5 feet of you with your shield.") )
    npc.append(Feature("Fast Shield", "If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you.") )
    npc.append(Reaction("Blast Shield", "If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect.") )
```
