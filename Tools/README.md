# Tools
This directory contains a number of Python scripts/apps (they start as scripts, and slowly I'm coming to the idea that they need to become full-fledged apps, so hey, let's test how well Python "scales up" that way eh?) for managing this repo.

## Long-term goals
A collection of tools for managing the repository.

Specifically, tools for managing:

* The magic spells available in the world
* The magic items available in the world
* The creatures that populate the world
* The "burbs" (cities, towns, and villages, large to small) that populate the world
* Quick-generated adventure ideas
* Calendar tracking; time and generated events that occur in the world as time passes
* NPC/Character generation: starting with traditional races, then other creatures/monsters(?)

## Website
Converts the Markdown content to static HTML for upload to a static site host (like Site44). 

Make sure mkdocs is installed: `pip3 install mkdocs`

From within the Website directory, run `mkdocs build`, or better yet just run `bake.sh` (a *nix shell script; you can use WSL2 on Windows but be prepared for slow bash file perf, welcome to WSL2) and it will do the work:

* Erase the old work
* Copy the entire repository contents into the Website/docs folder
* Run mkdocs on that folder without accidentally recursing infinitely
* Copy the resulting built files (in the `site` folder) over to the target directory (such as my Dropbox/Apps/Site44 directory) for upload. 
 
Note that by default it's going to `~/Dropbox/Apps/site44/azgaarnoth.tedneward.com`, unless there is a `sitetarget` file that contains a new target path. (Contents of that file are slurped up entirely whole, so no comments or anything allowed.)

Everything except the Tools and Supplements directory goes up into the website.

## FUTURE
Eventually, Spelltool, NPCGen, CityGen should all be classes/modules invoked from a master app. Maybe a Tk GUI app? Hm.

CLITool:
  --parsemd {dir}: Use Markdown as source material
  --parsesql {db}: Use SQLite db as source material
  --emitmd {dir}: Emit results (if any) to {dir} in Markdown
  --emitsql {db}: Emit results (if any) to SQLite {db}

## Design Notes
Backgrounds, Classes, Creatures, Equipment, Feats, Races should all be modules that are dynamically loaded and invoked. The top-level script in turn is responsible for bootstrapping the rest of the module, so for example, `Races/index.md` would load the various races (and from there, sub-races), and provide an opaque API for figuring out racial characteristics.

Standardized StatBlock type, with extensible sections for the various parts that matter to class-based types. Includes saving/loading to/from various forms: MD, SQLite, XML, plain text, ...?

Let's define per-module surface API ahead of time, to make it more consistent.

Each text "block" should be a Feature type, which has the titled-text format?

Feature (title + text)
+-- Trait
+-- Action
    +--- Attack?
    +--- Spellcasting?
+-- Reaction
+-- Bonus
+-- Lair

CharacterGen should allow for 100% randomization except for specified elements, so that I can specify anything (or nothing at all) to gen up an NPC. Randomization should be something invokable at any level (racial/sub-racial, class/subclass, background, etc).

### Later
Look into using a headless CMS for any/all of this? TinaCMS, for example?

Build a nicer/more-thematic CSS/HTML template for Website gen.

