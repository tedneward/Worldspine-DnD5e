# Races

```
name = "Races"
```

"Core" SRD Races

* [Dragonborn](Dragonborn)
* [Dwarves](Dwarves)
* [Elves](Elves)
* [Gnomes](Gnomes)
* [Half-Elves](Half-Elves)
* [Half-Orcs](Half-Orcs)
* [Halflings](Halflings)
* [Humans](Humans)
* [Tieflings](Tieflings)

Commonly-accepted/extended Races

* [Bugbears](Bugbears)
* [Goblins](Goblins)
* [Hobgoblins](Hobgoblins)
* [Kobolds](Kobolds)
* [Lizardfolk](Lizardfolk)
* [Minotaurs](Minotaurs)
* [Orcs](Orcs)
* [Tabaxi](Tabaxi)
* [Tortles](Tortles)

```
# A list of all languages spoken in the world
languages = {
    'Common': ['Common', 'Dwarvish', 'Elvish', 'Gnomish', 'Goblin', 'Halfling', 'Orc'],
    'Exotic': ['Abyssal', 'Celestial', 'Draconic', 'Deep Speech', 'Infernal', 
               'Primordial','Aquan', 'Auran', 'Ignan', 'Terran',
               'Sylvan', 'Undercommon' ]
}
def languagelist(which = 'All'):
    if which == 'All': return languages['Common'] + languages['Exotic']
    else: return languages[which]

def chooselanguage(npc, which='Common'):
    srclist = languagelist(which).copy()
    for lang in npc.languages:
        if lang in srclist:
            srclist.remove(lang)

    chosen = choose("Choose a language: ", srclist)
    npc.languages.append(chosen)

def random(npc):
    racemod = randomfrom(childmods)

    print("I chose a",racemod.name,"for you, boss!")
    npc.setrace(racemod)
    npc.race.random(npc) #subrace choice should come in here, if possible/necessary

exports = [ languagelist, chooselanguage ]
```
