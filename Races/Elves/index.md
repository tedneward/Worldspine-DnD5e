# Race: Elves
See [*Elves*](../../Creatures/Elves.md) for more details.

Elves are a magical people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.

## Slender and Graceful
With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and members of many other races. They are slightly shorter than humans on average, ranging from well under 5 feet tall to just over 6 feet. They are more slender than humans, weighing only 100 to 145 pounds. Males and females are about the same height, and males are only marginally heavier than females.

Elves’ coloration encompasses the normal human range and also includes skin in shades of copper, bronze, and almost bluish-white, hair of green or blue, and eyes like pools of liquid gold or silver. Elves have no facial and little body hair. They favor elegant clothing in bright colors, and they enjoy simple yet lovely jewelry.

## A Timeless Perspective
Elves can live well over 700 years, giving them a broad perspective on events that might trouble the shorter-lived races more deeply. They are more often amused than excited, and more likely to be curious than greedy. They tend to remain aloof and unfazed by petty happenstance. When pursuing a goal, however, whether adventuring on a mission or learning a new skill or art, elves can be focused and relentless. They are slow to make friends and enemies, and even slower to forget them. They reply to petty insults with disdain and to serious insults with vengeance.

Like the branches of a young tree, elves are flexible in the face of danger. They trust in diplomacy and compromise to resolve differences before they escalate to violence. They have been known to retreat from intrusions into their woodland homes, confident that they can simply wait the invaders out. But when the need arises, elves reveal a stern martial side, demonstrating skill with sword, bow, and strategy.

## Hidden Woodland Realms
Most elves dwell in small forest villages hidden among the trees. Elves hunt game, gather food, and grow vegetables, and their skill and magic allow them to support themselves without the need for clearing and plowing land. They are talented artisans, crafting finely worked clothes and art objects. Their contact with outsiders is usually limited, though a few elves make a good living by trading crafted items for metals (which they have no interest in mining).

Elves encountered outside their own lands are commonly traveling minstrels, artists, or sages. Human nobles compete for the services of elf instructors to teach swordplay or magic to their children.

## Exploration and Adventure
Elves take up adventuring out of wanderlust. Since they are so long-lived, they can enjoy centuries of exploration and discovery. They dislike the pace of human society, which is regimented from day to day but constantly changing over decades, so they find careers that let them travel freely and set their own pace. Elves also enjoy exercising their martial prowess or gaining greater magical power, and adventuring allows them to do so. Some might join with rebels fighting against oppression, and others might become champions of moral causes.


```
name = 'Elf'
description = "***Race: Elf.*** Elves are a magical people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music and poetry, and the good things of the world."
type = 'humanoid'
```

* **Ability Score Increase**. Your Dexterity score increases by 2.

* **Age**. Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 25 and most can live to be 150 years old.

* **Alignment**. Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and are good more often than not.

* **Size**. Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Fey Ancestry**. You have advantage on saving throws against being charmed, and magic can't put you to sleep.

* **Trance**. Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.

* **Keen Senses**. You have proficiency in the Perception skill.

* **Languages**. You can speak, read, and write Common and Elven.

```
def apply(npc):
    npc.DEX += 2

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.append(Feature("Fey Ancestry", "You have advantage on saving throws against being charmed, and magic can't put you to sleep."))
    npc.conditionimmunities.append("sleep")

    npc.append(Feature("Trance", "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance'. While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.") )

    npc.addproficiency("Perception")

    npc.languages.append("Common")
    npc.languages.append("Elven")
```

Elves have a number of genetically-differentiated offshoots (subraces):

* [High Elves](Elves/High.md)
* [Wood Elves](Elves/Wood.md)

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

## Elvish Names
Elves are considered children until they declare themselves adults, some time after the hundredth birthday, and before this period they are called by child names.

On declaring adulthood, an elf selects an adult name, although those who knew him or her as a youngster might continue to use the child name. Each elf’s adult name is a unique creation, though it might reflect the names of respected individuals or other family members. Little distinction exists between male names and female names; the groupings here reflect only general tendencies. In addition, every elf bears a family name, typically a combination of other Elvish words. Some elves traveling among humans translate their family names into Common, but others retain the Elvish version.

**Child Names:** Ara, Bryn, Del, Eryn, Faen, Innil, Lael, Mella, Naill, Naeris, Phann, Rael, Rinn, Sai, Syllin, Thia, Vall

**Male Adult Names:** Adran, Aelar, Aramil, Arannis, Aust, Beiro, Berrian, Carric, Enialis, Erdan, Erevan, Galinndan, Hadarai, Heian, Himo, Immeral, Ivellios, Laucian, Mindartis, Paelias, Peren, Quarion, Riardon, Rolen, Soveliss, Thamior, Tharivol, Theren, Varis

**Female Adult Names:** Adrie, Althaea, Anastrianna, Andraste, Antinua, Bethrynna, Birel, Caelynn, Drusilia, Enna, Felosial, Ielenia, Jelenneth, Keyleth, Leshanna, Lia, Meriele, Mialee, Naivara, Quelenna, Quillathe, Sariel, Shanairra, Shava, Silaqui, Theirastra, Thia, Vadania, Valanthe, Xanaphia

**Family Names (Common Translations):** Amakiir (Gemflower), Amastacia (Starflower), Galanodel (Moonwhisper), Holimion (Diamonddew), Ilphelkiir (Gemblossom), Liadon (Silverfrond), Meliamne (Oakenheel), Naïlo (Nightbreeze), Siannodel (Moonbrook), Xiloscient (Goldpetal)

```
def get_name(npc):
    def firstname():
        male_names = [
            'Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 
            'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 
            'Erevan', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 
            'Immeral', 'Ivellios', 'Laucian', 'Mindartis', 
            'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 
            'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'
        ]
        female_names = [
            'Adrie', 'Althaea', 'Anastrianna', 'Andraste', 
            'Antinua', 'Bethrynna', 'Birel', 'Caelynn', 'Drusilia', 
            'Enna', 'Felosial', 'Ielenia', 'Jelenneth', 'Keyleth', 
            'Leshanna', 'Lia', 'Meriele', 'Mialee', 'Naivara', 
            'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava', 
            'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 
            'Xanaphia'
        ]
        if npc.gender == 'Male': return generatemarkovname(male_names)
        else: return generatemarkovname(female_names)

    def lastname():
        if randomint(0,1) == 0:
            familynames = [
                'Amakiir', 'Amastacia', 'Galanodel', 'Holimion', 
                'Ilphelkiir', 'Liadon', 'Meliamne', 'Nailo', 
                'Siannodel', 'Xiloscient'
            ]
            return generatemarkovname(familynames)
        else:
            # Elvish translated names are two-parters
            prenouns = [
                'gem','ruby','diamond','silver','gold',
                'star','moon','day','night',
                'river','lake','stream','pond',
            ]
            postnouns = [
                'flower','blossom','frond','brook','petal','dew',
                'whisper','wind','breeze',
                'heel',
            ]
            part1 = prenouns[randomint(0, len(prenouns)-1)].capitalize()
            part2 = postnouns[randomint(0, len(postnouns)-1)]
            return f"{part1}{part2}"

    return f"{firstname()} {lastname()}"
```
