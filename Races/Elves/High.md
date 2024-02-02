# High Elf
...

* **Ability Score Increase**. Your Intelligence score increases by 1.

* **Cantrip**. You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.

* **Elf Weapon Training**. You have proficiency with the longsword, shortsword, shortbow, and longbow.

* **Extra Language**. You can read, speak, and write one additional language of your choice.

```
name = 'High'
description = "***Subrace: High Elf.***"

class HighElfCasting(Action):
    def __init__(self, cantrip):
        Action.__init__(self, "Cantrip", "")
        self.cantrip = cantrip

    def __str__(self):
        text  = f"**Spell Save DC** {8 + self.npc.proficiencybonus() + self.npc.INTbonus()} "
        text += f"**Spell Attack Bonus** +{self.npc.proficiencybonus() + self.npc.INTbonus()}. "
        text += f"You know {spelllink(self.cantrip)} and can cast it at will."
        return text

def apply(npc):
    npc.INT += 1

    availablecantrips = [
        'acid splash', 'chill touch', 'dancing lights', 'fire bolt', 'light', 'mage hand',
        'mending', 'message', 'minor illusion', 'poison spray', 'prestidigitation',
        'ray of frost', 'shocking grasp', 'true strike'
    ]
    chosen = choose("Choose a cantrip:", availablecantrips)
    npc.append(HighElfCasting(chosen))

    npc.addproficiency("Longsword")
    npc.addproficiency("Shortsword")
    npc.addproficiency("Longbow")
    npc.addproficiency("Shortbow")

    chooselanguage(npc, 'Common')
```
