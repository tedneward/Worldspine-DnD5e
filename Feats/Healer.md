## Healer
You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight. You gain the following benefits:

* When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point.
* As an action. you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest.

```
name = 'Healer'
description = "***Feat: Healer.*** You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight."
def prereq(npc): return True
def apply(npc):
    npc.append(Feature("Healer", "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point.") )
    npc.append(Action("Healer", "You can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest.") )
```
