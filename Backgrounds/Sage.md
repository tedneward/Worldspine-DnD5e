# Background: Sage
You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you. Your efforts have made you a master in your fields of study.

```
name = "Sage"
description = "***Background: Sage.*** You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you. Your efforts have made you a master in your fields of study."
```

## Skill Proficiencies
Arcana, History

```
def apply(npc):
    npc.addproficiency("Arcana")
    npc.addproficiency("History")
```

## Languages
Two of your choice

```
    chooselanguage(npc)
    chooselanguage(npc)
```

## Equipment
A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a pouch containing 10 gp

```
    npc.addequipment("A bottle of black ink")
    npc.addequipment("A quill")
    npc.addequipment("A small knife")
    npc.addequipment("A letter from a dead colleague posing a question you have not yet been able to answer")
```

## Specialty
To determine the nature of your scholarly training, roll a d8 or choose from the options in the table below.

d8| Specialty
--| ----
1 | Alchemist
2 | Astronomer
3 | Discredited academic
4 | Librarian
5 | Professor
6 | Researcher
7 | Wizard's apprentice
8 | Scribe

```
    specialty = [ 
        'Alchemist', 'Astronomer', 'Discredited academic', 'Librarian',
        'Professor', 'Researcher', "Wizard's apprentice", "Scribe",
    ]
    npc.description.append(f"***Criminal Specialty: {randomfrom(specialty)}.***")
```


## Feature: Researcher
When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign.

```
    npc.append(Feature("Researcher", "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."))
```

## Suggested Characteristics
Sages are defined by their extensive studies, and their characteristics reflect this life of study. Devoted to scholarly pursuits, a sage values knowledge highly — sometimes in its own right, sometimes as a means toward other ideals.

d8| Personality Trait
--| -----------------
1 | I use polysyllabic words that convey the impression of great erudition.
2 | I've read every book in the world's greatest libraries — or I like to boast that I have.
3 | I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.
4 | There's nothing I like more than a good mystery.
5 | I'm willing to listen to every side of an argument before I make my own judgment.
6 | I... speak... slowly... when talking... to idiots, ... which... almost... everyone... is... compared... to me.
7 | I am horribly, horribly awkward in social situations.
8 | I'm convinced that people are always trying to steal my secrets.

```
    traits = [
        "I use polysyllabic words that convey the impression of great erudition.",
        "I've read every book in the world's greatest libraries — or I like to boast that I have.",
        "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
        "There's nothing I like more than a good mystery.",
        "I'm willing to listen to every side of an argument before I make my own judgment.",
        "I... speak... slowly... when talking... to idiots, ... which... almost... everyone... is... compared... to me.",
        "I am horribly, horribly awkward in social situations.",
        "I'm convinced that people are always trying to steal my secrets.",
    ]
    npc.description.append(f"***Personality Trait.*** {randomfrom(traits)}")
```

d6| Ideal
--| ----
1 | **Knowledge.** The path to power and self-improvement is through knowledge. (Neutral)
2 | **Beauty.** What is beautiful points us beyond itself toward what is true. (Good)
3 | **Logic.** Emotions must not cloud our logical thinking. (Lawful)
4 | **No Limits.** Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)
5 | **Power.** Knowledge is the path to power and domination. (Evil)
6 | **Self-Improvement.** The goal of a life of study is the betterment of oneself. (Any)

```
    ideals = [
        ["Knowledge","The path to power and self-improvement is through knowledge.","Neutral"],
        ["Beauty","What is beautiful points us beyond itself toward what is true.","Good"],
        ["Logic","Emotions must not cloud our logical thinking.","Lawful"],
        ["No Limits","Nothing should fetter the infinite possibility inherent in all existence.","Chaotic"],
        ["Power","Knowledge is the path to power and domination.","Evil"],
        ["Self-Improvement","The goal of a life of study is the betterment of oneself.","Any"],
    ]
    ideal = ideals[randomint(0, len(ideals) - 1)]
    npc.description.append(f"***Ideal: {ideal[0]}.*** {ideal[1]}")
    if ideal[2] != "Any": npc.alignment = "any " + ideal[2]
```

d6| Bond
--| ----
1 | It is my duty to protect my students.
2 | I have an ancient text that holds terrible secrets that must not fall into the wrong hands.
3 | I work to preserve a library, university, scriptorium, or monastery.
4 | My life's work is a series of tomes related to a specific field of lore.
5 | I've been searching my whole life for the answer to a certain question.
6 | I sold my soul for knowledge. I hope to do great deeds and win it back.

```
    bonds = [
        "It is my duty to protect my students.",
        "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "I work to preserve a library, university, scriptorium, or monastery.",
        "My life's work is a series of tomes related to a specific field of lore.",
        "I've been searching my whole life for the answer to a certain question.",
        "I sold my soul for knowledge. I hope to do great deeds and win it back.",
    ]
    npc.description.append(f"***Bond.*** {randomfrom(bonds)}")
```

d6| Flaw
--| ----
1 | I am easily distracted by the promise of information.
2 | Most people scream and run when they see a demon. I stop and take notes on its anatomy.
3 | Unlocking an ancient mystery is worth the price of a civilization.
4 | I overlook obvious solutions in favor of complicated ones.
5 | I speak without really thinking through my words, invariably insulting others.
6 | I can't keep a secret to save my life, or anyone else's.

```
    flaws = [
        "I am easily distracted by the promise of information.",
        "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "Unlocking an ancient mystery is worth the price of a civilization.",
        "I overlook obvious solutions in favor of complicated ones.",
        "I speak without really thinking through my words, invariably insulting others.",
        "I can't keep a secret to save my life, or anyone else's.",
    ]
    npc.description.append(f"***Flaw.*** {randomfrom(flaws)}")
```
