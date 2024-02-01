# Subrace: High Elf
One of your parents was a High Elf.

***Cantrip.*** You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.

***Elf Weapon Training.*** You have proficiency with the longsword, shortsword, shortbow, and longbow.

```
name = 'High'
description = "***Subrace: High Elf.*** One of your parents was a High Elf."

class CantripCasting(Action):
    def __init__(self, cantrip):
        Action.__init__(self, "Cantrip", "")
        self.cantrip = cantrip

    def __str__(self):
        text  =  "***High Elf Cantrip.*** "
        text += f"You know {spelllink(self.cantrip)} and can cast it at will. "
        text += f"**Spell Save DC** {8 + self.npc.proficiencybonus() + self.npc.INTbonus()} "
        text += f"**Spell Attack Bonus** +{self.npc.proficiencybonus() + self.npc.INTbonus()}."
        return text

def apply(npc):
    availablecantrips = [
        'acid splash', 'chill touch', 'dancing lights', 'fire bolt', 'light', 'mage hand',
        'mending', 'message', 'minor illusion', 'poison spray', 'prestidigitation',
        'ray of frost', 'shocking grasp', 'true strike'
    ]
    chosen = choose("Choose a cantrip:", availablecantrips)
    npc.append(CantripCasting(chosen))

    npc.addproficiency("Longsword")
    npc.addproficiency("Shortsword")
    npc.addproficiency("Longbow")
    npc.addproficiency("Shortbow")
```
