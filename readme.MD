# Final Fantasy XIV - Basic Crafting Bot

This is a simple crafting bot for Final Fantasy XIV.  In it's most basic sense, this script sends predefined series of keystrokes to the currently active window.  As such, it can not be run in the background, FFXIV must remain the primary window of focus.

 ## General setup

 The bot is hard coded with the locations of expected crafting spells.  Following are a set of macros that will place the needed spells in their required locations.

 ```
/hotbar action "Muscle Memory" 1 1
/hotbar action "Rapid Synthesis" 1 2
/hotbar action "Basic Synthesis" 1 3
/hotbar action "Careful Synthesis" 1 4
/hotbar action "Delicate Synthesis" 1 5
/hotbar action "Reuse" 1 6
/hotbar action "Hasty Touch" 1 7
/hotbar action "Basic Touch" 1 8
/hotbar action "Standard Touch" 1 9
/hotbar action "Preparatory Touch" 1 10
/hotbar action "Patient Touch" 1 11
/hotbar action "Collectable Synthesis" 1 12

/hotbar action "Name of the Elements" 2 1
/hotbar action "Brand of the Elements" 2 2
/hotbar action "Intensive Synthesis" 2 3
/hotbar action "Focused Synthesis" 2 5
/hotbar action "Observe" 2 6
/hotbar action "Focused Touch" 2 7
/hotbar action "Precise Touch" 2 8
/hotbar action "Prudent Touch" 2 9
/hotbar action "Byregot's Blessing" 2 10
/hotbar action "Trained Eye" 2 12

/hotbar action "Master's Mend" 3 1
/hotbar action "Final Appraisal" 3 2
/hotbar action "Waste Not" 3 3
/hotbar action "Waste Not II" 3 4
/hotbar action "Manipulation" 3 5
/hotbar action "Careful Observation" 3 6
/hotbar action "Tricks of the Trade" 3 7
/hotbar action "Great Strides" 3 8
/hotbar action "Innovation" 3 9
/hotbar action "Reflect" 3 10
/hotbar action "Ingenuity" 3 11
/hotbar action "Inner Quiet" 3 12

/hotbar copy current 1 CRP 1
/hotbar copy current 1 BSM 1
/hotbar copy current 1 ARM 1
/hotbar copy current 1 GSM 1
/hotbar copy current 1 LTW 1
/hotbar copy current 1 WVR 1
/hotbar copy current 1 ALC 1
/hotbar copy current 1 CUL 1

/hotbar copy current 2 CRP 2
/hotbar copy current 2 BSM 2
/hotbar copy current 2 ARM 2
/hotbar copy current 2 GSM 2
/hotbar copy current 2 LTW 2
/hotbar copy current 2 WVR 2
/hotbar copy current 2 ALC 2
/hotbar copy current 2 CUL 2

/hotbar copy current 3 CRP 3
/hotbar copy current 3 BSM 3
/hotbar copy current 3 ARM 3
/hotbar copy current 3 GSM 3
/hotbar copy current 3 LTW 3
/hotbar copy current 3 WVR 3
/hotbar copy current 3 ALC 3
/hotbar copy current 3 CUL 3
```

## Usage

As this is just a keypress bot, setup is required for proper use.

The current point of this bot is to automate the creation of multiple similar items - i.e. you want to produce 20 Ethereal Silk while AFK.

The bot expects you initially to be already be crafting an item - you've selected the materials you wish to use, and clicked "synthesize".  It's not intelligent enough to change the materias is you run out of your HQ / NQ, so have all that prepared ahead of time.

Run the script, select the crafting function you wish to use, and specify the quantity to craft.  After pressing return you will have three seconds to select the FFXIV window before the bot begins sending keystrokes.