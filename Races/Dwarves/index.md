# Race: Dwarves
See [*Dwarves*](../../Creatures/Dwarves.md) for more details.

Kingdoms rich in ancient grandeur, halls carved into the roots of mountains, the echoing of picks and hammers in deep mines and blazing forges, a commitment to clan and tradition, and a burning hatred of goblins and orcs — these common threads unite all dwarves.

### Short and Stout
Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal. Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller. Their courage and endurance are also easily a match for any of the larger folk.

Dwarven skin ranges from deep brown to a paler hue tinged with red, but the most common shades are light brown or deep tan, like certain tones of earth. Their hair, worn long but in simple styles, is usually black, gray, or brown, though paler dwarves often have red hair. Male dwarves value their beards highly and groom them carefully.

### Long Memory, Long Grudges
Dwarves can live to be more than 400 years old, so the oldest living dwarves often remember a very different world. For example, some of the oldest dwarves living in Citadel Felbarr (in the world of the Forgotten Realms) can recall the day, more than three centuries ago, when orcs conquered the fortress and drove them into an exile that lasted over 250 years. This longevity grants them a perspective on the world that shorter-lived races such as humans and halflings lack.

Dwarves are solid and enduring like the mountains they love, weathering the passage of centuries with stoic endurance and little change. They respect the traditions of their clans, tracing their ancestry back to the founding of their most ancient strongholds in the youth of the world, and don't abandon those traditions lightly. Part of those traditions is devotion to the gods of the dwarves, who uphold the dwarven ideals of industrious labor, skill in battle, and devotion to the forge.

Individual dwarves are determined and loyal, true to their word and decisive in action, sometimes to the point of stubbornness. Many dwarves have a strong sense of justice, and they are slow to forget wrongs they have suffered. A wrong done to one dwarf is a wrong done to the dwarf's entire clan, so what begins as one dwarf's hunt for vengeance can become a full-blown clan feud.

### Clans and Kingdoms
Dwarven kingdoms stretch deep beneath the mountains where the dwarves mine gems and precious metals and forge items of wonder. They love the beauty and artistry of precious metals and fine jewelry, and in some dwarves this love festers into avarice. Whatever wealth they can't find in their mountains, they gain through trade. They dislike boats, so enterprising humans and halflings frequently handle trade in dwarven goods along water routes. Trustworthy members of other races are welcome in dwarf settlements, though some areas are off limits even to them.

The chief unit of dwarven society is the clan, and dwarves highly value social standing. Even dwarves who live far from their own kingdoms cherish their clan identities and affiliations, recognize related dwarves, and invoke their ancestors' names in oaths and curses. To be clanless is the worst fate that can befall a dwarf.

Dwarves in other lands are typically artisans, especially weaponsmiths, armorers, and jewelers. Some become mercenaries or bodyguards, highly sought after for their courage and loyalty.

### Gods, Gold, and Clan
Dwarves who take up the adventuring life might be motivated by a desire for treasure — for its own sake, for a specific purpose, or even out of an altruistic desire to help others. Other dwarves are driven by the command or inspiration of a deity, a direct calling or simply a desire to bring glory to one of the dwarf gods. Clan and ancestry are also important motivators. A dwarf might seek to restore a clan's lost honor, avenge an ancient wrong the clan suffered, or earn a new place within the clan after having been exiled. Or a dwarf might search for the axe wielded by a mighty ancestor, lost on the field of battle centuries ago.

```
name = 'Dwarf'
description = "***Race: Dwarf.*** Dwarves are solid and enduring like the mountains they love, weathering the passage of centuries with stoic endurance and little change. They respect the traditions of their clans, tracing their ancestry back to the founding of their most ancient strongholds in the youth of the world, and don't abandon those traditions lightly. Part of those traditions is devotion to the gods of the dwarves, who uphold the dwarven ideals of industrious labor, skill in battle, and devotion to the forge."
type = 'humanoid'
```

* **Ability Score Increase**. Your Constitution score increases by 2.

* **Age**. Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 35. On average, they live about 150 years.

* **Alignment**. Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.

* **Size**. Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.

* **Darkvision**. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Dwarven Resilience**. You have advantage on saving throws against poison, and you have resistance against poison damage.

* **Dwarven Combat Training**. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.

* **Tool Proficiency**. You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.

* **Stonecunning**. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.

* **Languages**. You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.

```
def apply(npc):
    npc.CON += 2
    npc.size = 'Medium'
    npc.speed['walking'] = 25
    npc.senses['darkvision'] = 60
    npc.damageresistances.append('poison')
    npc.append(Feature("Dwarven Resilience", "You have advantage on saving throws against poison."))
    npc.append(Feature("Stonecunning", "Whenever you make an Intelligence (History) check related to the origin of stonework, it is considered proficient in the History skill and add doubles its proficiency bonus to the check."))

    # TODO: Add these from the roots['Equipment'] weapons?
    npc.addproficiency(Equipment.weapons['melee']['Battleaxe'].name)
    npc.addproficiency(Equipment.weapons['melee']['Warhammer'].name)
    npc.addproficiency(Equipment.weapons['melee']['Handaxe'].name)
    npc.addproficiency(Equipment.weapons['melee']['Light hammer'].name)

    toolchoice = choose("Choose a tool proficiency:", ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"])
    npc.addproficiency(toolchoice)
```

Dwarves have a number of genetically-differentiated offshoots (subraces):

* [Hill](Hill.md)
* [Mountain](Mountain.md)


```
def random(npc):
    subracemod = randomfrom(childmods)
    print("I choose a",subracemod.name,npc.race.name,"for you, boss!")
    npc.setsubrace(subracemod)
```

## Physical Attributes

### Height

```
def get_height(npc):
    pass
```

### Weight

```
def get_weight(npc):
    pass
```

## Dwarf Names
A dwarf's name is granted by a clan elder, in accordance with tradition. Every proper dwarven name has been used and reused down through the generations. A dwarf's name belongs to the clan, not to the individual. A dwarf who misuses or brings shame to a clan name is stripped of the name and forbidden by law to use any dwarven name in its place.

**Male Names:** Adrik, Alberich, Baern, Barendd, Brottor, Bruenor, Dain, Darrak, Delg, Eberk, Einkil, Fargrim, Flint, Gardain, Harbek, Kildrak, Morgran, Orsik, Oskar, Rangrim, Rurik, Taklinn, Thoradin, Thorin, Tordek, Traubon, Travok, Ulfgar, Veit, Vondal

**Female Names:** Amber, Artin, Audhild, Bardryn, Dagnal, Diesa, Eldeth, Falkrunn, Finellen, Gunnloda, Gurdis, Helja, Hlin, Kathra, Kristryd, Ilde, Liftrasa, Mardred, Riswynn, Sannl, Torbera, Torgga, Vistra

**Clan Names:** Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart

```
def get_name(npc):
    def firstname():
        male_names = [
            'Adrik', 'Alaron', 'Alberich', 'Aldrek', 'Ardo',
            'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Barazak', 
            'Balur', 'Bombur', 'Bofur', 'Bnar',
            'Chakrir', 'Carnir', 'Cadmael',
            'Dain', 'Darrak', 'Delg', 'Dendirsyr', 'Dorn', 'Dophensus',
            'Eberk', 'Einkil','Erwid', 'Erli', 'Ednir',
            'Fargrim', 'Flint', 'Farsben', 'Fili', 'Fordreth', 'Fenzig',
            'Gardain', 'Gadaric', 'Gimli', 'Graflyn', 'Gunder', 
            'Goltan', 'Grimn', 'Grisbane',
            'Harbek', 'Haldrik', 'Heimoc', 'Helsbid', 'Helwright', 'Hoskuld',
            'Kalhor', 'Karsten', 'Kenth', 'Kili', 'Kulderik', 'Kellan', 'Kardnyr', 'Krael',
            'Kall', 'Kildrak',
            'Lornir', 'Lorik', 'Laron',
            'Maarik', 'Meli', 'Mostyr', 'Morgran',
            'Nomir',
            'Ostrin', 'Orsik', 'Oskar',
            'Ryonn', 'Rangrim', 'Rurik',
            'Taklinn', 'Thoradin', 'Tordek', 'Traubon', 'Travok',
            'Thorin', 'Thordrik', 'Thorstyr', 'Thaladan', 'Tomir',
            'Ulfgar',
            'Valamar', 'Valdan', 'Veit', 'Vondal'
        ]
        female_names = [
            'Amber', 'Artin', 'Audhild', 
            'Bardryn', 
            'Dagnal', 'Diesa', 
            'Eldeth', 
            'Falkrunn', 'Finellen', 
            'Gunnloda', 'Gurdis', 
            'Helja', 'Hlin', 
            'Ilde', 
            'Kathra', 'Kristryd', 
            'Liftrasa', 
            'Mardred', 
            'Riswynn', 
            'Sannl', 
            'Torbera', 
            'Torgga', 
            'Vistra'
        ]
        if npc.gender == 'Male': return generatemarkovname(male_names)
        else: return generatemarkovname(female_names)

    def lastname():
        # Dwarven lastnames are often two-parters
        prenouns = [
            'strong', 'steady', 'barren',
            'mountain','hill','cliff','range','mine','crag','storm','root',
            'sword', 'spear', 'axe', 'hammer',
            'two', 'three', 'four',
            'battle','war',
            'shaft', 'haft',
            'wolf', 'bear', 'tiger', 'rat', 'troll', 'dragon',
            'eagle','raven','hawk','hen',
            'brown', 'gray', 'green', 'black', 'red',
            'coal', 'shale', 'iron', 'oak', 'steel', 'gravel',
            'wooden','oaken','ivy',
            'fire','earth','air','water','lightning','thunder','psychic',
        ]
        postnouns = [
            'mountain','hill','cliff','range','mine','crag','storm','root',
            'gates','shaft','tower',
            'sword','spear','axe','hammer', 'shield',
            'hand','tongue','skull','blood', 'fist',
            'talon','claw','beak','hawk',
            'borne','heim','bane','battle',
            'pants','vest','tunic','shirt',
            'smith','shadow',
        ]
        verbs = [
            'breaker','smiter','hewer','slasher','stealer','smasher'
        ]
        if randomint(0,1) == 0:
            part1 = prenouns[randomint(0, len(prenouns)-1)].capitalize()
            part2 = postnouns[randomint(0, len(postnouns)-1)]
            return f"{part1}{part2}"
        else:
            part1 = prenouns[randomint(0, len(prenouns)-1)].capitalize()
            part2 = verbs[randomint(0, len(verbs)-1)]
            return f"{part1}{part2}"
    return f"{firstname()} {lastname()}"
```
