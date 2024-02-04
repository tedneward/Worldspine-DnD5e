# Humans
Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human's memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics.

```
name = 'Human'
description = "***Race: Human.*** Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human's memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics."
type = 'humanoid'
```

* **Ability Score Increase.** Two of your ability scores each increase by 1.

* **Age.** Humans reach adulthood in their late teens and live less than a century.

* **Size.** Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Skills.** You gain proficiency in one skill of your choice.

* **Feat.** You gain one [Feat](../../Feats/) of your choice.

* **Languages.** You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.

```
def apply(npc):
    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.languages.append("Common")

    abilityscoreincrease(npc)
    abilityscoreincrease(npc)

    chooselanguage(npc, 'Common')

    chooseskill(npc)

    choosefeat(npc)

def random(npc): pass
```

## Physical Attributes

### Height
Male: 5 feet minimum (usually), 6 1/2 feet maximum (usually)
Female: 4 1/2 feet minimum (usually), 6 feet maximum (usually)

### Weight
Male:
Female:

```    
def generateheight():
    pass

def generateweight():
    pass
```

## Human Names
Having so much more variety than other cultures, humans as a whole have no typical names. Some human parents give their children names from other languages, such as Dwarvish or Elvish (pronounced more or less correctly), but most parents give names that are linked to their region's culture or to the naming traditions of their ancestors.

The material culture and physical characteristics of humans can change wildly from region to region. In the Forgotten Realms, for example, the clothing, architecture, cuisine, music, and literature are different in the northwestern lands of the Silver Marches than in distant Turmish or Impiltur to the east — and even more distinctive in far-off Kara-Tur. Human physical characteristics, though, vary according to the ancient migrations of the earliest humans, so that the humans of the Silver Marches have every possible variation of coloration and features.

```
# From https://www.roll4.net/generators/dd-name-generators/dnd-human-name-generator
def get_name(npc):
    def firstname():
        female_names = [
            'Ustice','Ey','Pari','Cora','Ulia','Lla','La','Hali','Zoe','Jeanor','Ypri',
            'Charle','Zie','Ker','Xaris','Ta','Premila'
        ]
        male_names = [
            'Pert','Quincy','Son','Junter','Jonald','Ver','Xan','Eonald','Oinn','Hannon',
            'Isdel','Del','Yer','Ylis','Yaelan','Arker','Wan','Adler','Camen','Caseer',
            'Premilan','Ulan','Xaris','Tayler','Lyn'
        ]
        if npc.gender=='Female': return generatemarkovname(female_names)
        else: return generatemarkovname(male_names)
    
    def lastname():
        if randomint(0,1) == 0:
            # Markov-generated name
            last_names = [
                'We','Ynn','Mpson','Va','Wang','Aross','Barrin','Yncano','Guerre','Krajas',
                'Ser','Guerra','An','Pez','Pruz','Ussen','Corte','Ton','Ubbott','Na','Gers',
                'Quinn','Crosby','Sam','Rince','Ke','Quez','Quinne','Goosethorn'
            ]
            return generatemarkovname(last_names)
        else:
            # Two-parter name
            prenouns = [
                'winter','snake','ice','camel','fall',
                'oath','jaguar','croc','wind','tiger',
                'lion','bear','star','light','morning',
                'crane','wolf'
            ]
            postnouns = [
                'screamer','wing','striker','crawl','seeker',
                'break','chaser','hold','wind','bone','love',
                'forge','binder','punch','guts'
            ]
            part1 = prenouns[randomint(0, len(prenouns)-1)].capitalize()
            part2 = postnouns[randomint(0, len(postnouns)-1)]
            return f"{part1}{part2}"

    return f"{firstname()} {lastname()}" 
```
