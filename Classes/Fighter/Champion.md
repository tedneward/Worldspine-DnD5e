# Martial Archetype: Champion
The archetypal Champion focuses on the development of raw physical power honed to deadly perfection. Those who model themselves on this archetype combine rigorous training with physical excellence to deal devastating blows.

```
name = 'Champion'
description = "***Martial Archetype: Champion.*** The archetypal Champion focuses on the development of raw physical power honed to deadly perfection. Those who model themselves on this archetype combine rigorous training with physical excellence to deal devastating blows."
```

## Improved Critical
*3rd-level Champion feature*

Your weapon attacks score a critical hit on a roll of 19 or 20.

```
def level3(npc):
    npc.append(Feature("Improved Critical", "Your weapon attacks score a critical hit on a roll of 19-20.") )
```

## Remarkable Athlete
*7th-level Champion feature*

You can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus.

In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier.

```
def level7(npc):
    npc.append(Feature("Remarkable Athlete", "You can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier.") )
```

## Additional Fighting Style
*10th-level Champion feature*

You can choose a second option from the Fighting Style class feature.

```
def level10(npc):
    parent.choosestyle(npc)
```

## Superior Critical
*15th-level Champion feature*

Your weapon attacks score a critical hit on a roll of 18-20.

```
def level15(npc):
    npc.append(Feature("Improved Critical", "Your weapon attacks score a critical hit on a roll of 18-20.") )
```

## Survivor
*18th-level Champion feature*

You attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points.

```
def level18(npc):
    npc.append(Feature("Survivor", "At the start of each of your turns, you regain {5 + self.npc.CONbonus()} hit points if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."))
```
