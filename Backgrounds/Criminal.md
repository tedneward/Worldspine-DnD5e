# Background: Criminal
You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the criminal underworld. You’re far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society.

```
name = "Criminal"
description = "***Background: Criminal.**** You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the criminal underworld. You’re far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society."
```

## Variant: Spy
You might have appeared to others to be a criminal, but the truth was far more complex: Your extensive history in breaking or circumventing the law was always on behalf of others (your country, your faction, your religion, or something more exotic). Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context. You're far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society.

You might have been an officially sanctioned agent of the crown, or perhaps you sold the secrets you uncovered to the highest bidder, and your relationship to your spymasters can be either lapsed, burned, betrayed, or still active.

```
def apply(npc):
    if dieroll(1,100) > 75:
        description = "***Background: Spy.*** You might have appeared to others to be a criminal, but the truth was far more complex: Your extensive history in breaking or circumventing the law was always on behalf of others (your country, your faction, your religion, or something more exotic). Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context. You're far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society."
```

## Skill Proficiencies: 
Deception, Stealth

```
def apply(npc):
    npc.addproficiency("Deception")
    npc.addproficiency("Stealth")
```

## Tool Proficiencies
One type of gaming set, thieves’ tools

```
    npc.addproficiency("Gaming set")
    npc.addproficiency("Thieves' tools")
```

## Equipment
A crowbar, a set of dark common clothes including a hood, and a pouch containing 15 gp

```
    npc.addequipment("Crowbar")
    npc.addequipment("Set of dark common clothes including a hood")
```

## Criminal Specialty
There are many kinds of criminals, and within a thieves’ guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others. Choose the role you played in your criminal life, or roll on the table below.

d8| Specialty
--| ---------
1 | Blackmailer
2 | Burglar
3 | Enforcer
4 | Fence
5 | Highway robber
6 | Hired killer
7 | Pickpocket
8 | Smuggler

```
    specialty = [ 
        'Blackmailer', 'Burglar', 'Enforcer', 'Fence', 
        'Highway robber', 'Hired killer', 'Pickpocket', 'Smuggler'
    ]
    npc.description.append(f"***Criminal Specialty: {randomfrom(specialty)}.***")
```

## Feature: Criminal Contact
You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you.

```
    npc.append(Feature("Criminal Contact", "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."))
```

d8| Personality Trait
--| -----------------
1 | I always have a plan for what to do when things go wrong.
2 | I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.
3 | The first thing I do in a new place is note the locations of everything valuable — or where such things could be hidden.
4 | I would rather make a new friend than a new enemy.
5 | I am incredibly slow to trust. Those who seem the fairest often have the most to hide.
6 | I don't pay attention to the risks in a situation. Never tell me the odds.
7 | The best way to get me to do something is to tell me I can't do it.
8 | I blow up at the slightest insult.

```
    traits = [
        "I always have a plan for what to do when things go wrong.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "The first thing I do in a new place is note the locations of everything valuable — or where such things could be hidden.",
        "I would rather make a new friend than a new enemy.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I blow up at the slightest insult."
    ]
    npc.description.append(f"***Personality Trait.*** {randompick(traits)}")
```

d6| Ideal
--| -----
1 | **Honor.** I don't steal from others in the trade. (Lawful)
2 | **Freedom.** Chains are meant to be broken, as are those who would forge them. (Chaotic)
3 | **Charity.** I steal from the wealthy so that I can help people in need. (Good)
4 | **Greed.** I will do whatever it takes to become wealthy. (Evil)
5 | **People.** I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)
6 | **Redemption.** There's a spark of good in everyone. (Good)

```
    ideals = [
        ["Honor", "I don't steal from others in the trade.", "Lawful"],
        ["Freedom", "Chains are meant to be broken, as are those who would forge them.", "Chaotic"],
        ["Charity", "I steal from the wealthy so that I can help people in need.", "Good"],
        ["Greed", "I will do whatever it takes to become wealthy.", "Evil"]
        ["People", "I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.", "Neutral"],
        ["Redemption", "There's a spark of good in everyone.", "Good"]
    ]
    ideal = randompick(ideals)
    npc.description.append(f"***Ideal: {ideal[0]}.*** {ideal[1]}")
    npc.alignment = "any " + ideal[2]
```

d6| Bond
--| ----
1 | I'm trying to pay off an old debt I owe to a generous benefactor.
2 | My ill-gotten gains go to support my family.
3 | Something important was taken from me, and I aim to steal it back.
4 | I will become the greatest thief that ever lived.
5 | I'm guilty of a terrible crime. I hope I can redeem myself for it.
6 | Someone I loved died because of I mistake I made. That will never happen again.

```
    bonds = [
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "My ill-gotten gains go to support my family.",
        "Something important was taken from me, and I aim to steal it back.",
        "I will become the greatest thief that ever lived.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "Someone I loved died because of I mistake I made. That will never happen again."
    ]
    npc.description.append(f"***Bond.*** {randomfrom(bonds)}")
```

d6| Flaw
--| ----
1 | When I see something valuable, I can't think about anything but how to steal it.
2 | When faced with a choice between money and my friends, I usually choose the money.
3 | If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.
4 | I have a “tell” that reveals when I'm lying.
5 | I turn tail and run when things look bad.
6 | An innocent person is in prison for a crime that I committed. I'm okay with that.

```
    flaws = [
        "When I see something valuable, I can't think about anything but how to steal it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "I have a 'tell' that reveals when I'm lying.",
        "I turn tail and run when things look bad.",
        "An innocent person is in prison for a crime that I committed. I'm okay with that."
    ]
    npc.description.append(f"***Flaw.*** {randomfrom(flaws)}")
```
