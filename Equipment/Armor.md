# Equipment: Armor
*Cost* indicates the going rate for said armor, assuming it is purchased in a Major City (population > 25,000) and all materials are easily available.

*Armor Class* indicates the armor class for the creature wearing it. "+ Dex" means the creature adds its full Dexterity attribute bonus to AC; "+Dex (max 2)" means the creature gets, at most, a +2 bonus for its Dexterity. If Dex is not mentioned, then the armor is too bulky to benefit from Dexterity.

*Strength* indicates the minimum Strength score a creature must have in order to wear this armor.

*Stealth* indicates any Advantage or Disadvantage to Stealth checks when wearing this armor.

*Weight* describes the total weight to the armor once donned.

```
armor = {}
```

## Light Armor
Made from supple and thin materials, light armor favors agile adventurers since it offers some protection without sacrificing mobility. If you wear light armor, you add your Dexterity modifier to the base number from your armor type to determine your Armor Class.

Name        | Cost | Armor Class | Strength | Stealth | Weight
----------- | ---- | ----------- | -------- | ------- | ------
[Leather](#leather) | 10 gp | 11 + Dex | - | - | 10 lb.
[Padded](#padded) | 5 gp | 11 + Dex | - | Disadvantage | 8 lb.
[Studded leather](#studded-leather) | 45 gp | 12 + Dex | - | - | 13 lb.

## Medium Armor
Medium armor offers more protection than light armor, but it also impairs movement more. If you wear medium armor, you add your Dexterity modifier, to a maximum of +2, to the base number from your armor type to determine your Armor Class.

Name         | Cost | Armor Class | Strength | Stealth | Weight
------------ | ---- | ----------- | -------- | ------- | ------
[Hide](#hide) | 10 gp | 12 + Dex (max 2) | - | - | 12 lb.
[Chain shirt](#chain-shirt) | 50 gp | 13 + Dex (max 2) | - | - | 20 lb.
[Scale mail](#scale-mail) | 50 gp | 14 + Dex (max 2) | - | Disadvantage | 45 lb.
[Breastplate](#breastplate) | 400 gp | 14 + Dex (max 2) | - | - | 20 lb.
[Half plate](#half-plate) | 750 gp | 15 + Dex (max 2) | - | Disadvantage | 40 lb.

## Heavy Armor
Of all the armor categories, heavy armor offers the best protection. These suits of armor cover the entire body and are designed to stop a wide range of attacks. Only proficient warriors can manage their weight and bulk.

Heavy armor doesn’t let you add your Dexterity modifier to your Armor Class, but it also doesn’t penalize you if your Dexterity modifier is negative.

Name        | Cost | Armor Class | Strength | Stealth | Weight
----------- | ---- | ----------- | -------- | ------- | ------
[Ring mail](#ring-mail) | 30 gp | 14 | - | Disadvantage | 40 lb.
[Chain mail](#chain-mail) | 75 gp | 16 | Str 13 | Disadvantage | 55 lb.
[Splint](#splint) | 200 gp | 17 | Str 15 | Disadvantage | 60 lb.
[Plate](#plate) | 1,500 gp | 18 | Str 15 | Disadvantage | 65 lb.

## Shields
A shield is often made from wood or metal and is either carried in one hand or strapped to that hand. You can benefit from only one shield at a time.

Name        | Cost | Armor Class | Strength | Stealth | Weight
----------- | ---- | ----------- | -------- | ------- | ------
[Shield](#shield) | 10 gp | +2 | - | - | 6 lb.


#### Breastplate
This armor consists of a fitted metal chest piece worn with supple leather. Although it leaves the legs and arms relatively unprotected, this armor provides good protection for the wearer’s vital organs while leaving the wearer relatively unencumbered.

#### Chain mail
Made of interlocking metal rings, chain mail includes a layer of quilted fabric worn underneath the mail to prevent chafing and to cushion the impact of blows. The suit includes gauntlets.

#### Chain shirt
Made of interlocking metal rings, a chain shirt is worn between layers of clothing or leather. This armor offers modest protection to the wearer’s upper body and allows the sound of the rings rubbing against one another to be muffled by outer layers.

#### Half plate
Half plate consists of shaped metal plates that cover most of the wearer’s body. It does not include leg protection beyond simple greaves that are attached with leather straps.

#### Hide
This crude armor consists of thick furs and pelts.

#### Leather
The breastplate and shoulder protectors of this armor are made of leather that has been stiffened by being boiled in oil. The rest of the armor is made of softer and more flexible materials.

#### Padded
Padded armor consists of quilted layers of cloth and batting.

#### Plate
Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body.

#### Ring mail
This armor is leather armor with heavy rings sewn into it. The rings help reinforce the armor against blows from swords and axes. Ring mail is inferior to chain mail, and it’s usually worn only by those who can’t afford better armor.

#### Scale mail
This armor consists of a coat and leggings (and perhaps a separate skirt) of leather covered with overlapping pieces of metal, much like the scales of a fish. The suit includes gauntlets.

#### Shield
A shield is made from wood or metal and is carried in one hand. Wielding a shield increases your Armor Class by 2. You can benefit from only one shield at a time.

#### Splint
This armor is made of narrow vertical strips of metal riveted to a backing of leather that is worn over cloth padding. Flexible chain mail protects the joints.

#### Studded leather
Made from tough but flexible leather, studded leather is reinforced with close-set rivets or spikes.

```
armor = {
    'light': {
        'Battle robe' : 11,
        'Padded armor' : 11, 
        'Leather armor' : 11,
        'Leather lamellar' : 12,
        'Studded leather armor' : 12
    },
    'medium': {
        'Hide armor' : 12, 
        'Chain shirt' : 13,
        'Plated leather' : 13,
        'Wood' : 13,
        'Scale mail' : 14, 
        'Breastplate' : 14, 
        'Half-plate' : 15,
        'Kozane' : 15
    },
    'heavy': {
        'Ring mail' : 14,
        'Lorica segmentata' : 15,
        'Chain mail' : 16,
        'Splint armor' : 17,
        'Plate armor' : 18
    },
    'shields': {
        'Buckler' : 1,
        'Fencing cloak' : 1,
        'Vambrace' : 1,
        'Shield' : 2,
        'Tower shield' : 2
    }
}

def init():
    parent.armor = armor
```
