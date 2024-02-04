# Equipment: Weapons

```
weapons = {}

class Weapon:
    def __init__(self, name, weight, dmg, dmgtype, properties=[]):
        self.name = name
        self.weight = weight
        self.dmg = dmg
        self.dmgtype = dmgtype
        self.properties = properties

    def findproperty(self, property):
        for prop in self.properties:
            if property in prop:
                return prop
        return None

    def getactions(self): pass

    def getnameorstr(self,obj):
        if isinstance(obj, Weapon): return obj.name
        else: return obj

    def __lt__(self, obj): return ((self.name) < self.getnameorstr(obj)) 
    def __gt__(self, obj): return ((self.name) > self.getnameorstr(obj)) 
    def __le__(self, obj): return ((self.name) <= self.getnameorstr(obj)) 
    def __ge__(self, obj): return ((self.name) >= self.getnameorstr(obj)) 
    def __eq__(self, obj): return (self.name == self.getnameorstr(obj)) 
  
    def __repr__(self): return str((self.name, self.weight, self.dmg, self.dmgtype, self.properties))
        
    def __str__(self): return f"{self.name} ({self.weight} lb)"

class MeleeWeapon(Weapon):
    def __init__(self, name, weight, dmg, dmgtype, properties=[]):
        Weapon.__init__(self, name, weight, dmg, dmgtype, properties)

    def getactions(self):
        # If the weapon has 'finesse', just pass it on to the attack action
        actions = [ MeleeAttack(self.name, self.dmg, self.dmgtype, self.properties) ]

        # If the weapon has 'two-handed', make note of that in the action description
        twohanded = self.findproperty('two-handed')
        if twohanded != None:
            actions = [ MeleeAttack(self.name + " (Two-Handed)", self.dmg, self.dmgtype, self.properties) ]

        # If the weapon has 'versatile', it can be used one- or two-handed
        versatile = self.findproperty('versatile')
        if versatile != None:
            dmg = versatile[len("versatile "):][1:-1]
            actions.append(MeleeAttack(self.name + " (Two-Handed)", dmg, self.dmgtype, self.properties))

        # If the weapon has 'reach', it's reach is doubled
        reach = self.findproperty('reach')
        if reach != None:
            actions[0].reach = "10ft"

        return actions

class RangedWeapon(Weapon):
    def __init__(self, name, weight, range, dmg, dmgtype, properties=[]):
        Weapon.__init__(self, name, weight, dmg, dmgtype, properties)
        self.range = range

    def getactions(self):
        return [ RangedAttack(self.name, self.range, self.dmg, self.dmgtype) ]

class ThrowableWeapon(Weapon):
    def __init__(self, name, weight, range, dmg, dmgtype, properties=[]):
        Weapon.__init__(self, name, weight, dmg, dmgtype, properties)
        self.range = range

    def getactions(self):
        return [
            MeleeAttack(self.name, self.dmg, self.dmgtype, self.properties),
            RangedAttack(self.name + " (Thrown)", self.range, self.dmg, self.dmgtype)
        ]
```

## Simple Melee Weapons

Name | Cost | Damage | Weight | Properties | Block
---- | ---- | ------ | ------ | ---------- | -------
Club | 1 sp | 1d4 bludgeoning | 2 lb. | Light | ***Club.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d4 + {STRbonus} bludgeoning damage.
Dagger | 2 gp | 1d4 piercing | 1 lb. | Finesse, light, thrown (20/60) | ***Dagger.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus|DEXbonus} to hit, 5ft., one target. Hit: 1d4 + {STRbonus|DEXbonus} piercing damage. *Ranged Weapon Attack:* +{proficiency bonus + DEXbonus} to hit, range 20/60, one target. Hit: 1d4 + {DEX bonus} piercing damage.
Greatclub | 2 sp | 1d8 bludgeoning | 10 lb. | Two-handed | ***Greatclub.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d8 + {STRbonus} bludgeoning damage.
Handaxe | 5 gp | 1d6 slashing | 2 lb. | Light, thrown (20/60) | ***Handaxe.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d6 + {STRbonus} slashing damage. *Ranged Weapon Attack:* +{proficiency bonus + STRbonus} to hit, range 20/60, one target. Hit: 1d6 + {STR bonus} slashing damage.
Javelin | 5 sp | 1d6 piercing | 2 lb. | Thrown (30/120) | ***Javelin.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d6 + {STRbonus} piercing damage. *Ranged Weapon Attack:* +{proficiency bonus + STRbonus} to hit, range 30/120, one target. Hit: 1d6 + {STR bonus} piercing damage.
Light hammer | 2 gp | 1d4 bludgeoning | 2 lb. | Light, thrown (20/60) | ***Light hammer.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d4 + {STRbonus} bludgeoning damage. *Ranged Weapon Attack:* +{proficiency bonus + STRbonus} to hit, range 20/60, one target. Hit: 1d4 + {STR bonus} bludgeoning damage.
Mace | 5 gp | 1d6 bludgeoning | 4 lb. | — | ***Mace.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d6 + {STRbonus} bludgeoning damage.
Quarterstaff | 2 sp | 1d6 bludgeoning | 4 lb. | Versatile (1d8) | ***Quarterstaff.*** *Melee Weapon Attack (one-handed):* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d6 + {STRbonus} bludgeoning damage. *Melee Weapon Attack (two-handed):* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d8 + {STRbonus} bludgeoning damage.
Sickle | 1 gp | 1d4 slashing | 2 lb. | Light | ***Sickle.*** *Melee Weapon Attack:* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d4 + {STRbonus} slashing damage.
Spear | 1 gp | 1d6 piercing | 3 lb. | Thrown (20/60), versatile (1d8) | ***Spear.*** *Melee Weapon Attack (one-handed):* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d4 + {STRbonus} piercing damage. *Melee Weapon Attack (two-handed):* +{proficiency bonus + STRbonus} to hit, 5ft., one target. Hit: 1d8 + {STRbonus} piercing damage. *Ranged Weapon Attack:* +{proficiency bonus + STRbonus} to hit, range 20/60, one target. Hit: 1d6 + {STR bonus} piercing damage.

```
weapons['simple-melee'] = {
    'Club': MeleeWeapon("Club", "2", '1d4', 'bludgeoning', ['light']),
    'Dagger': ThrowableWeapon("Dagger", "1", '20/60', '1d4', 'piercing', ['finesse','light','thrown']),
    'Greatclub': MeleeWeapon("Greatclub", "10", '1d8', 'bludgeoning', ['two-handed']),
    'Handaxe': ThrowableWeapon("Handaxe", "2", '20/60', '1d6', 'slashing', ['light', 'thrown']),
    'Javelin': ThrowableWeapon("Javelin", "2", '30/120', '1d6', 'piercing', ['thrown']),
    'Light hammer': ThrowableWeapon("Light hammer", "2", '20/60', '1d4', 'bludgeoning', ['light','thrown']),
    'Mace': MeleeWeapon("Mace", "4", '1d6', 'bludgeoning'),
    'Quarterstaff': MeleeWeapon("Quarterstaff", "4", '1d6', 'bludgeoning', ['versatile (1d8)']),
    'Sickle': MeleeWeapon("Sickle", "2", '1d4', 'slashing', ['light']),
    'Spear': ThrowableWeapon("Spear", "3", '20/60', '1d6', 'piercing', ['thrown', 'versatile (1d8)']),
}
```

## Martial Melee Weapons

Name | Cost | Damage | Weight | Properties | Block
---- | ---- | ------ | ------ | ---------- | -------
Battleaxe | 10 gp | 1d8 slashing | 4 lb. | Versatile (1d10) | 
Flail | 10 gp | 1d8 bludgeoning | 2 lb. | — | 
Glaive | 20 gp | 1d10 slashing | 6 lb. | Heavy, reach, two-handed | 
Greataxe | 30 gp | 1d12 slashing | 7 lb. | Heavy, two-handed | 
Greatsword | 50 gp | 2d6 slashing | 6 lb. | Heavy, two-handed | 
Halberd | 20 gp | 1d10 slashing | 6 lb. | Heavy, reach, two-handed | 
Lance | 10 gp | 1d12 piercing | 6 lb. | Reach, special | 
Longsword | 15 gp | 1d8 slashing | 3 lb. | Versatile (1d10) | 
Maul | 10 gp | 2d6 bludgeoning | 10 lb. | Heavy, two-handed | 
Morningstar | 15 gp | 1d8 piercing | 4 lb. | — | 
Pike | 5 gp | 1d10 piercing | 18 lb. | Heavy, reach, two-handed | 
Rapier | 25 gp | 1d8 piercing | 2 lb. | Finesse | 
Scimitar | 25 gp | 1d6 slashing | 3 lb. | Finesse, light | 
Shortsword | 10 gp | 1d6 piercing | 2 lb. | Finesse, light | 
Trident | 5 gp | 1d6 piercing | 4 lb. | Thrown (20/60), versatile (1d8) | 
War pick | 5 gp | 1d8 piercing | 2 lb. | — | 
Warhammer | 15 gp | 1d8 bludgeoning | 2 lb. | versatile (1d10) | 
Whip | 2 gp | 1d4 slashing | 3 lb. | Finesse, reach | 

```
weapons['martial-melee'] = {
    'Battleaxe': MeleeWeapon("Battleaxe", "4", '1d8', 'slashing', ['versatile (1d10)']),
    'Flail': MeleeWeapon("Flail", "2", '1d8', 'bludgeoning'),
    'Glaive': MeleeWeapon("Glaive", "6", '1d10', 'slashing', ['heavy', 'reach', 'two-handed']),
    'Greataxe': MeleeWeapon("Greataxe", "7", '1d12', 'slashing', ['heavy', 'two-handed']),
    'Greatsword': MeleeWeapon("Greatsword", "6", '2d6', 'slashing', ['heavy', 'two-handed']),
    'Halberd': MeleeWeapon("Halberd", "6", '1d10', 'slashing', ['heavy', 'reach', 'two-handed']),
    'Lance': MeleeWeapon("Lance", "6", '1d12', 'piercing', ['reach', 'special']),
    'Longsword': MeleeWeapon("Longsword", "3", '1d8', 'slashing', ['versatile (1d10)']),
    'Maul': MeleeWeapon("Maul", "10", '2d6', 'bludgeoning', ['heavy', 'two-handed']),
    'Morningstar': MeleeWeapon("Morningstar", "4", '1d8', 'piercing'),
    'Pike': MeleeWeapon("Pike", "18", '1d10', 'piercing', ['heavy', 'reach', 'two-handed']),
    'Rapier': MeleeWeapon("Rapier", "2", '1d8', 'piercing', ['finesse']),
    'Scimitar': MeleeWeapon("Scimitar", "3", '1d6', 'slashing', ['finesse', 'light']),
    'Shortsword': MeleeWeapon("Shortsword", "2", '1d6', 'piercing', ['finesse', 'light']),
    'Trident': ThrowableWeapon("Trident", "4", '20/60', '1d6', 'piercing', ['versatile (1d8)']),
    'War pick': MeleeWeapon("War pick", "2", '1d8', 'piercing'),
    'Warhammer': MeleeWeapon("Warhammer", "2", '1d8', 'bludgeoning', ['versatile (1d10)']),
    'Whip': MeleeWeapon("Whip", "3", '1d4', 'slashing', ['finesse', 'reach']),
}
```

## Simple Ranged Weapons

Name | Cost | Damage | Weight | Properties | Block
---- | ---- | ------ | ------ | ---------- | -------
Crossbow, light | 25 gp | 1d8 piercing | 5 lb. | Ammunition, range (80/320), loading, two-handed | 
Dart | 5 cp | 1d4 piercing | 1/4 lb. | Finesse, thrown (20/60) | 
Shortbow | 25 gp | 1d6 piercing | 2 lb. | Ammunition, range (80/320), two-handed | 
Sling | 1 sp | 1d4 piercing | — | Ammunition, range (30/120) | 

```
weapons['simple-ranged'] = {
    'Light Crossbow': RangedWeapon("Light Crossbow", "5", '80/320', '1d8', 'piercing', ['ammunition', 'loading', 'two-handed']),
    'Dart': RangedWeapon("Dart", "1/4", '20/60', '1d4', 'piercing', ['finesse', 'thrown']),
    'Javelin': ThrowableWeapon("Javelin", "2", '30/120', '1d6', 'piercing', ['thrown']),
    'Shortbow': RangedWeapon("Shortbow", "2", '80/320', '1d6', 'piercing', ['ammunition', 'two-handed']),
    'Sling': RangedWeapon("Sling", "-", '30/120', '1d4', 'bludgeoning', ['ammunition']),
}
```

## Martial Ranged Weapons

Name | Cost | Damage | Weight | Properties | Block
---- | ---- | ------ | ------ | ---------- | -------
Blowgun | 10 gp | 1 piercing | 1 lb. | Ammunition, range (25/100), loading | 
Crossbow, hand | 75 gp | 1d6 piercing | 3 lb. | Ammunition, range (30/120), light, loading | 
Crossbow, heavy | 50 gp | 1d10 piercing | 18 lb. | Ammunition, range (100/400), heavy, loading, two-handed | 
Longbow | 50 gp | 1d8 piercing | 2 lb. | Ammunition, range (150/600), heavy, two-Handed | 
Net | 1 gp | — | 3 lb. | Special, thrown (5/15) | 

```
weapons['martial-ranged'] = {
    'Blowgun': RangedWeapon("Blowgun", "1", '25/100', '1', 'piercing', ['ammunition', 'loading']),
    'Hand crossbow': RangedWeapon("Hand Crossbow", "3", '30/120', '1d6', 'piercing', ['ammunition', 'light', 'loading']),
    'Heavy crossbow': RangedWeapon("Heavy Crossbow", "18", '100/400', '1d10', 'piercing', ['ammunition', 'heavy', 'loading', 'two-handed']),
    'Longbow': RangedWeapon("Longbow", "2", '150/600', '1d8', 'piercing', ['ammunition', 'heavy', 'two-handed']),
    'Net': RangedWeapon("Net", "3", '5/15', '0', 'special')
}
```

## Ammunition

Ammunition | Cost | Weight
---------- | ---- | ---------
Arrows (20) | 1 gp | 1 lb.
Blowgun needles (50) | 1 gp | 1 lb.
Crossbow bolts (20) | 1 gp | 1.5 lb.
Sling bullets (20) | 4 cp | 1.5 lb.

```
weapons['martial'] = weapons['martial-melee'] | weapons['martial-ranged']
weapons['simple'] = weapons['simple-melee'] | weapons['simple-ranged']
weapons['melee'] = weapons['simple-melee'] | weapons['martial-melee']
weapons['ranged'] = weapons['simple-ranged'] | weapons['martial-ranged']
weapons['all'] = weapons['simple'] | weapons['martial']
```

## Weapon Properties
Many weapons have special properties related to their use, as shown in the Weapons tables above.

Property | Description
-------- | --------------
Ammunition | You can use a weapon that has the ammunition property to make a ranged attack only if you have ammunition to fire from the weapon. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack. Loading a one-handed weapon requires a free hand. At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield. If you use a weapon that has the ammunition property to make a melee attack, you treat the weapon as an improvised weapon. A sling must be loaded to deal any damage when used in this way.
Finesse | When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.
Heavy | Creatures that are Small or Tiny have disadvantage on attack rolls with heavy weapons. A heavy weapon's size and bulk make it too large for a Small or Tiny creature to use effectively.
Light | A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.
Loading | Because of the time required to load this weapon, you can fire only one piece of ammunition from it when you use an action, bonus action, or reaction to fire it, regardless of the number of attacks you can normally make.
Range | A weapon that can be used to make a ranged attack has a range shown in parentheses after the ammunition or thrown property. The range lists two numbers. The first is the weapon's normal range in feet, and the second indicates the weapon's maximum range. When attacking a target beyond normal range, you have disadvantage on the attack roll. You can't attack a target beyond the weapon's long range.
Reach | This weapon adds 5 feet to your reach when you attack with it. This property also determines your reach for opportunity attacks with a reach weapon.
Special | A weapon with the special property has unusual rules governing its use, explained in the weapon's description (See below)
Thrown | If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.
Two-Handed | This weapon requires two hands to use. This property is relevant only when you attack with the weapon, not when you simply hold it.
Versatile | This weapon can be used with one or two hands. A damage value in parentheses appears with the property—the damage when the weapon is used with two hands to make a melee attack.

```
def init():
    parent.weapons = weapons

exports = { Weapon, MeleeWeapon, RangedWeapon }
```
