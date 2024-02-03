## Linguist
You have studied languages and codes, gaining the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You learn three languages of your choice.
* You can ably create written ciphers. Others can't decipher a code you create unless you teach them, they succeed on an Intelligence check (DC equal to your Intelligence score + your proficiency bonus), or they use magic to decipher it.

```
name = 'Linguist'
description = "***Feat: Linguist.*** You have studied languages and codes."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    chooselanguage(npc, 'All')
    chooselanguage(npc, 'All')
    chooselanguage(npc, 'All')

    npc.append(Feature("Encipher", "You can create written ciphers. Others can't decipher a code you create unless you teach them, they succeed on an Intelligence check (DC {self.npc.INT + self.npc.proficiencybonus()}), or they use magic to decipher it.") )
```
