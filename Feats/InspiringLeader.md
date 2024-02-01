## Inspiring Leader
*Prerequisite: Charisma 13 or higher*

You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature can gain temporary hit points equal to your level + your Charisma modifier. A creature can't gain temporary hit points from this feat again until it has finished a short or long rest.

```
name = 'Inspiring Leader'
description = "***Feat: Inspiring Leader.*** You can inspire people to greater resolve."
def prereq(npc): return npc.CHA >= 13
def apply(npc):
    npc.append(Feature("Inspiring Leader", "You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature can gain {self.npc.levels() + self.npc.CHAbonus()} temporary hit points. A creature can't gain temporary hit points from this feat again until it has finished a short or long rest.") )
```

