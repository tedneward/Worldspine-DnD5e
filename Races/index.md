# Races

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

def random():
    #print("Picking a race at random from ", modules, " boss!")
    (name, race) = randomfrom(modules)
    if getattr(race, "subraces", None) != None:
        (name, subrace) = randomfrom(race.subraces)
        print("I picked a", subrace.name, race.name, "for you, boss!")
        return (race, subrace)
    else:
        print("I picked a", race.name, "for you, boss!")
        return race
```
