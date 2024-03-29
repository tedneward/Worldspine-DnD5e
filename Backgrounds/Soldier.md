# Background: Soldier
War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, learned basic survival techniques, including how to stay alive on the battlefield. You might have been part of a standing national army or a mercenary company, or perhaps a member of a local militia who rose to prominence during a recent war.

When you choose this background, work with your DM to determine which military organization you were a part of, how far through its ranks you progressed, and what kind of experiences you had during your military career. Was it a standing army, a town guard, or a village militia? Or it might have been a noble's or merchant's private army, or a mercenary company.

```
name = "Soldier"
description = "***Background: Soldier.*** War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, learned basic survival techniques, including how to stay alive on the battlefield. You might have been part of a standing national army or a mercenary company, or perhaps a member of a local militia who rose to prominence during a recent war."
```

## Skill Proficiencies
Athletics, Intimidation

```
def apply(npc):
    npc.addproficiency("Athletics")
    npc.addproficiency("Intimidation")
```

## Tool Proficiencies
One type of gaming set, vehicles (land)

```
    npc.addproficiency("Gaming set")
    npc.addproficiency("Vehicles (land)")
```

## Equipment
An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a set of bone dice or deck of cards, a set of common clothes, and a pouch containing 10 gp

```
    npc.addequipment("An insignia of rank")
    npc.addequipment("A trophy taken from a fallen enemy")
    npc.addequipment("A set of bone dice or deck of cards")
```

## Specialty
During your time as a soldier, you had a specific role to play in your unit or army. Roll a d8 or choose from the options in the table below to determine your role:

d8|Specialty
--|---------
1|Officer
2|Scout
3|Infantry
4|Cavalry
5|Healer
6|Quartermaster
7|Standard bearer
8|Support staff (cook, blacksmith, or the like)

## Feature: Military Rank
You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized.

```
    npc.append(Feature("Military Rank", "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."))
```

## Suggested Characteristics
The horrors of war combined with the rigid discipline of military service leave their mark on all soldiers, shaping their ideals, creating strong bonds, and often leaving them scarred and vulnerable to fear, shame, and hatred.

d8| Personality Trait
--| -----------------
1 | I'm always polite and respectful.
2 | I'm haunted by memories of war. I can't get the images of violence out of my mind.
3 | I've lost too many friends, and I'm slow to make new ones.
4 | I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.
5 | I can stare down a hell hound without flinching.
6 | I enjoy being strong and like breaking things.
7 | I have a crude sense of humor.
8 | I face problems head-on. A simple, direct solution is the best path to success.

```
    traits = [
        "I'm always polite and respectful.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I can stare down a hell hound without flinching.",
        "I enjoy being strong and like breaking things.",
        "I have a crude sense of humor.",
        "I face problems head-on. A simple, direct solution is the best path to success.",
    ]
    npc.description.append(f"***Personality Trait.*** {randomfrom(traits)}")
```

d6|Ideal
--|-----
1|Greater Good. Our lot is to lay down our lives in defense of others. (Good)
2|Responsibility. I do what I must and obey just authority. (Lawful)
3|Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)
4|Might. In life as in war, the stronger force wins. (Evil)
5|Live and Let Live. Ideals aren't worth killing over or going to war for. (Neutral)
6|Nation. My city, nation, or people are all that matter. (Any)

```
    ideals = [
        ["Greater Good","Our lot is to lay down our lives in defense of others.","Good"],
        ["Responsibility","I do what I must and obey just authority.","Lawful"],
        ["Independence","When people follow orders blindly, they embrace a kind of tyranny.","Chaotic"],
        ["Might","In life as in war, the stronger force wins.","Evil"],
        ["Live and Let Live","Ideals aren't worth killing over or going to war for.","Neutral"],
        ["Nation","My city, nation, or people are all that matter.","Any"],
    ]
    ideal = ideals[randomint(0, len(ideals) - 1)]
    npc.description.append(f"***Ideal: {ideal[0]}.*** {ideal[1]}")
    if ideal[2] != "Any": npc.alignment = "any " + ideal[2]
```

d6| Bond
--| ----
1 | I would still lay down my life for the people I served with.
2 | Someone saved my life on the battlefield. To this day, I will never leave a friend behind.
3 | My honor is my life.
4 | I'll never forget the crushing defeat my company suffered or the enemies who dealt it.
5 | Those who fight beside me are those worth dying for.
6 | I fight for those who cannot fight for themselves.

```
    bonds = [
        "I would still lay down my life for the people I served with.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "My honor is my life.",
        "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "Those who fight beside me are those worth dying for.",
        "I fight for those who cannot fight for themselves.",
    ]
    npc.description.append(f"***Bond.*** {randomfrom(bonds)}")
```

d6| Flaw
--| ----
1 | The monstrous enemy we faced in battle still leaves me quivering with fear.
2 | I have little respect for anyone who is not a proven warrior.
3 | I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret.
4 | My hatred of my enemies is blind and unreasoning.
5 | I obey the law, even if the law causes misery.
6 | I'd rather eat my armor than admit when I'm wrong.

```
    flaws = [
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I have little respect for anyone who is not a proven warrior.",
        "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret.",
        "My hatred of my enemies is blind and unreasoning.",
        "I obey the law, even if the law causes misery.",
        "I'd rather eat my armor than admit when I'm wrong.",
    ]
    npc.description.append(f"***Flaw.*** {randomfrom(flaws)}")
```
