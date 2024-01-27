# Humans
Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human’s memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics.

```
name = 'Human'
description = "***Race: Human.*** Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human’s memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics."
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

    roots['Abilities'].abilityscoreincrease(npc)
    roots['Abilities'].abilityscoreincrease(npc)

    roots['Races'].chooselanguage(npc)

    roots['Abilities'].chooseskill(npc)

    roots['Feats'].choosefeat(npc)

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

## Names
Human names span the gamut, often taking on cultural overtones, societal influences, and/or historical signficance.

Most humans have the typical surname/familyname pair, but some take on a singular nym for effect.

```
# From https://www.roll4.net/generators/dd-name-generators/dnd-human-name-generator
def generate_name(npc, gender):
    female_firstnames = [
        'Ustice','Ey','Pari','Cora','Ulia','Lla','La','Hali','Zoe','Jeanor','Ypri',
        'Charle','Zie','Ker','Xaris','Ta','Premila'
    ]
    male_firstnames = [
        'Pert','Quincy','Son','Junter','Jonald','Ver','Xan','Eonald','Oinn','Hannon',
        'Isdel','Del','Yer','Ylis','Yaelan','Arker','Wan','Adler','Camen','Caseer',
        'Premilan','Ulan','Xaris','Tayler','Lyn'
    ]
    
    last_names = [
        'We','Ynn','Mpson','Va','Wang','Aross','Barrin','Yncano','Guerre','Krajas',
        'Ser','Guerra','An','Pez','Pruz','Ussen','Corte','Ton','Ubbott','Na','Gers',
        'Quinn','Crosby','Sam','Rince','Ke','Quez','Quinne','Goosethorn',
        'Winterscreamer','Snakewing','Icestriker','Camelcrawl','Fallseeker',
        'Oathbreak','Jaguarscreamer','Crocchaser','Windhold','Tigerwind',
        'Tigerbone','Lionbone','Bearwind','Starlove','Lightforge','Morningbinder',
        'Cranepunch','Wolfguts'
    ]

    return (random(female_firstnames) if gender == 'female' else random(male_firstnames)) + random(last_names) 
```
