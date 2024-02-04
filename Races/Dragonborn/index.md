# Race: Dragonborn
*see [Dragonborn](../../Creatures/Dragonborn.md) for more details*

Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids. Some dragonborn are faithful servants to true dragons, others form the ranks of soldiers in great wars, and still others find themselves adrift, with no clear calling in life.

***Proud Dragon Kin.*** Dragonborn look very much like dragons standing erect in humanoid form, though they lack wings or a tail. The first dragonborn had scales of vibrant hues matching the colors of their dragon kin, but generations of interbreeding have created a more uniform appearance. Their small, fine scales are usually brass or bronze in color, sometimes ranging to scarlet, rust, gold, or copper-green. They are tall and strongly built, often standing close to 6 1/2 feet tall and weighing 300 pounds or more. Their hands and feet are strong, talonlike claws with three fingers and a thumb on each hand.

The blood of a particular type of dragon runs very strong through some dragonborn clans. These dragonborn often boast scales that more closely match those of their dragon ancestor — bright red, green, blue, or white, lustrous black, or gleaming metallic gold, silver, brass, copper, or bronze.

***Self-Sufficient Clans.*** To any dragonborn, the clan is more important than life itself. Dragonborn owe their devotion and respect to their clan above all else, even the gods. Each dragonborn's conduct reflects on the honor of his or her clan, and bringing dishonor to the clan can result in expulsion and exile. Each dragonborn knows his or her station and duties within the clan, and honor demands maintaining the bounds of that position.

A continual drive for self-improvement reflects the self-sufficiency of the race as a whole. Dragonborn value skill and excellence in all endeavors. They hate to fail, and they push themselves to extreme efforts before they give up on something. A dragonborn holds mastery of a particular skill as a lifetime goal. Members of other races who share the same commitment find it easy to earn the respect of a dragonborn.

Though all dragonborn strive to be self-sufficient, they recognize that help is sometimes needed in difficult situations. But the best source for such help is the clan, and when a clan needs help, it turns to another dragonborn clan before seeking aid from other races — or even from the gods.

```
name = 'Dragonborn'
description = "***Race: Dragonborn.*** Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids. Some dragonborn are faithful servants to true dragons, others form the ranks of soldiers in great wars, and still others find themselves adrift, with no clear calling in life."
type = 'humanoid'
```

***Ability Score Increase.*** Your Strength score increases by 2, and your Charisma score increases by 1.

***Age.*** Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.

***Alignment.*** Dragonborn tend towards extremes, making a conscious choice for one side or the other between Good and Evil (represented by Bahamut and Tiamat, respectively). More side with Bahamut than Tiamat (whose non-dragon followers are mostly kobolds), but villainous dragonborn can be quite terrible indeed. However, some dragonborn seek to distance themselves from their draconic heritage, and eschew the worship of either the Platinum or Chromatic Dragon, and instead prefer to dedicate themselves to another of the gods.

***Size.*** Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.

***Speed.*** Your base walking speed is 30 feet.

***Languages.*** You can read, speak, and write Common and Draconic.

```
def apply(npc):
    npc.STR += 2
    npc.CHA += 1
    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.languages.append('Common')
    npc.languages.append('Draconic')

class BreathWeapon(Action):
    def __init__(self, shape, dmgtype, save, damagetiers=['2d6','3d6','4d6','5d6'], title="Breath Weapon"):
        Action.__init__(self,title, "")
        self.recharges = "long rest"
        self.shape = shape
        self.dmgtype = dmgtype
        self.save = save
        self.dmgtiers = damagetiers
    
    def __str__(self):
        uses = self.npc.proficiencybonus()
        damage = ''
        if self.npc.levels() < 6: damage = self.dmgtiers[0]
        elif self.npc.levels() < 11: damage = self.dmgtiers[1]
        elif npc.levels() < 16: damage = self.dmgtiers[2]
        else: damage = self.dmgtiers[3]

        text += f"***{self.title} (Recharges on long rest).*** "
        text += f"You exhale destructive {self.dmgtype} in a {self.shape}. "
        text += f"All creatures in the area must make a {self.save} saving throw "
        text += f"(DC {8 + self.npc.CONbonus() + self.npc.proficiencybonus()}). "
        text += f"A creature takes {damage} {self.dmgtype} damage on a failed save, or half on a successful one."
        return text

class MetallicBreathWeapon(Action):
    def __init__(self):
        Action.__init__(self,"Metallic Breath Weapon", "")
        self.text = "You exhale a 15-foot cone of either Enervating Breath (Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn) or Repulsion Breath (Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone), DC {8 + self.npc.CONbonus() + self.npc.proficiencybonus()}."
        self.recharges = "long rest"

def breathweaponaction(shape, dmgtype, save): return BreathWeapon(shape, dmgtype, save)
def metallicbreathweaponaction(): return MetallicBreathWeapon()
```

## Draconic Ancestry
You are distantly related to a particular kind of dragon. Choose a type of dragon; this determines a variety of characteristics about your abilities. However, despite the general characteristics of a particular color of dragonborn, you are always free to establish your own characteristics (a noble and contemplative red, for example, or a selfish and violent gold.)

Dragonborn of chromatic colors are often chaotic, prone to violence, and sometimes selfish.

* [Black](Black.md)
* [Blue](Blue.md)
* [Green](Green.md)
* [Red](Red.md)
* [White](White.md)

Dragonborn of metallic colors are often law-abiding, slow to anger, and sometimes so noble you want to punch them in their perfect teeth.

* [Bronze](Bronze.md)
* [Brass](Brass.md)
* [Copper](Copper.md)
* [Gold](Gold.md)
* [Silver](Silver.md)

```
def random(npc):
    subracemod = randomfrom(childmods)
    print("I choose a",subracemod.name,npc.race.name,"for you, boss!")
    npc.setsubrace(subracemod)
```

## Physical Attributes

### Height

### Weight

## Dragonborn Names
Dragonborn have personal names given at birth, but they put their clan names first as a mark of honor. A childhood name or nickname is often used among clutchmates as a descriptive term or a term of endearment. The name might recall an event or center on a habit.

**Male Names:** Arjhan, Balasar, Bharash, Donaar, Ghesh, Heskan, Kriv, Medrash, Mehen, Nadarr, Pandjed, Patrin, Rhogar, Shamash, Shedinn, Tarhun, Torinn

**Female Names:** Akra, Biri, Daar, Farideh, Harann, Havilar, Jheri, Kava, Korinn, Mishann, Nala, Perra, Raiann, Sora, Surina, Thava, Uadjit

**Childhood Names:** Climber, Earbender, Leaper, Pious, Shieldbiter, Zealous

**Clan Names:** Clethtinthiallor, Daardendrian, Delmirev, Drachedandion, Fenkenkabradon, Kepeshkmolik, Kerrhylon, Kimbatuul, Linxakasendalor, Myastan, Nemmonis, Norixius, Ophinshtalajiir, Prexijandilin, Shestendeliath, Turnuroth, Verthisathurgiesh, Yarjerit

```
def get_name(npc, gender):
    def firstname():
        male_names = [
            'Arjhan', 'Balasar', 'Bharash', 'Donaar', 'Ghesh', 'Heskan', 
            'Kriv', 'Medrash', 'Mehen', 'Nadarr', 'Pandjed', 'Patrin', 
            'Rhogar', 'Shamash', 'Shedinn', 'Tarhun', 'Torinn'
        ]
        female_names = [
            'Akra', 'Biri', 'Daar', 'Farideh', 'Harann', 'Havilar', 
            'Jheri', 'Kava', 'Korinn', 'Mishann', 'Nala', 'Perra', 
            'Raiann', 'Sora', 'Surina', 'Thava', 'Uadjit'
        ]
        if npc.gender == 'Male': return generatemarkovname(male_names)
        else: return generatemarkovname(female_names)

    def lastname():
        clannames = [
            'Clethtinthiallor', 
            'Daardendrian', 'Delmirev', 'Drachedandion', 
            'Fenkenkabradon', 
            'Kepeshkmolik', 'Kerrhylon', 'Kimbatuul', 
            'Linxakasendalor', 
            'Myastan', 
            'Nemmonis', 'Norixius', 
            'Ophinshtalajiir',
            'Prexijandilin', 
            'Shestendeliath', 
            'Turnuroth', 
            'Verthisathurgiesh', 
            'Yarjerit'
        ]
        return generatemarkovname(clannames)

    return f"{firstname()} {lastname()}"
```

## Sample Dragonborn names (from https://www.roll4.net/generators/dd-name-generators/dragonborn-name-generator)
Worqir Narnok
Aqull Certha
Cacabi Tuapor
Thavil Shuanx
Iormas Eros
Drazav Folmac
Suwoph Uuxiro
Vyre Klichu
Thas Tualru
Faerqi Krun
Rashib Iccuuc
Lilofy Liltha
Jarn Fialra
Orlas Yuur
Naqrin Liltut
Qelnaa Iorzir
Gorax Dimin
Neslas Ilthur
Sulpra Nyuul
Perthi Craldu
Tazlzire Ernokenk
Pan Delith
Grigorax Porin
Otiyvyra Volmolda
Caerqiro Tharrhus
Kelskan Kiphikel
Sogwen Qek
Loralin On
Mar Axokeros
Krivriv Olmoker
Eragrax Shikelia
Pazavur Kriak
Zrariel Yor
Mibra Tir
Nagar Uuxoth
Zofshrin Pormec
Darre Enxenken
Naqiroth Liltheth
Viskan Kiphirer
Perlipor Draankon
Crish Lilthadi
Quiltqir Kar
Kahadurw Geadrial
Nagil Yuulkiar
Koxijen Nyuuldri
Halin Enxenxen
Dagar Lilthar
Cll Porrhisa
Gherash Axor
Erliprax Axon
Brensthi Dilthud
Valmbra Amruamti
Nadurwop Rhun
Eshriel Clec
Vissa Uuxash
Qiciar Guuxicho
Zora Fac
Beljhann Klual
Otivroth Narnajii
Otiyax Pruambuk
