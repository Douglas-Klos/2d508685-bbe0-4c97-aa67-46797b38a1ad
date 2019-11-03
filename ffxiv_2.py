import keyboard_scan_codes as ksc
from send_key import *

# General
menu_select = [ksc.KEY_NUMPAD0, None, .1]

# Crafting Spells
# Key, Modifier, Delay
muscle_memory = [ksc.KEY_1, None, 3, "Muscle Memory"]
rapid_synthesis = [ksc.KEY_2, None, 3, "Rapid Synthesis"]
basic_synthesis = [ksc.KEY_3, None, 3, "Basic Synthesis"]
careful_synthesis = [ksc.KEY_4, None, 3, "Careful Synthesis"]
delicate_synthesis = [ksc.KEY_5, None, 3, "Delicate Synthesis"]
reuse = [ksc.KEY_6, None, 3, "Reuse"]
hasty_touch = [ksc.KEY_7, None, 3, "Hasty Touch"]
basic_touch = [ksc.KEY_8, None, 3, "Basic Touch"]
standard_touch = [ksc.KEY_9, None, 3, "Standard Touch"]
preperatory_touch = [ksc.KEY_0, None, 3, "Preperatory Touch"]
patient_touch = [ksc.KEY_MINUS, None, 3, "Patient Touch"]
collectable_synthesis = [ksc.KEY_EQUALS, None, 2, "Collectable Synthesis"]

name_of_the_elements = [ksc.KEY_1, ksc.KEY_LSHIFT, 2, "Name of the Elements"]
brand_of_the_elements = [ksc.KEY_2, ksc.KEY_LSHIFT, 3, "Brand of the Elements"]
intensive_synthesis = [ksc.KEY_3, ksc.KEY_LSHIFT, 3, "Intensive Synthesis"]
focused_synthesis = [ksc.KEY_5, ksc.KEY_LSHIFT, 2, "Focused Synthesis"]
observe = [ksc.KEY_6, ksc.KEY_LSHIFT, 3, "Observe"]
focused_touch = [ksc.KEY_7, ksc.KEY_LSHIFT, 3, "Focused Touch"]
precise_touch = [ksc.KEY_8, ksc.KEY_LSHIFT, 3, "Precise Touch"]
prudent_touch = [ksc.KEY_9, ksc.KEY_LSHIFT, 3, "Prudent Touch"]
byregots_blessing = [ksc.KEY_0, ksc.KEY_LSHIFT, 3, "Byregot's Blessing"]
trained_eye = [ksc.KEY_EQUALS, ksc.KEY_LSHIFT, 3, "Trained Eye"]

masters_mend = [ksc.KEY_1, ksc.KEY_LCONTROL, 2, "Master's Mend"]
final_apprasial = [ksc.KEY_2, ksc.KEY_LCONTROL, 2, "Final Apprasial"]
waste_not = [ksc.KEY_3, ksc.KEY_LCONTROL, 2, "Waste Not"]
waste_not_2 = [ksc.KEY_4, ksc.KEY_LCONTROL, 2, "Waste Not 2"]
manipulation = [ksc.KEY_5, ksc.KEY_LCONTROL, 2, "Manipulation"]
careful_observation = [ksc.KEY_6, ksc.KEY_LCONTROL, 2, "Careful Observation"]
tricks_of_the_trade = [ksc.KEY_7, ksc.KEY_LCONTROL, 3, "Tricks of the Trade"]
great_strides = [ksc.KEY_8, ksc.KEY_LCONTROL, 2, "Great Strides"]
innovation = [ksc.KEY_9, ksc.KEY_LCONTROL, 2, "Innovation"]
reflect = [ksc.KEY_0, ksc.KEY_LCONTROL, 3, "Reflect"]
ingenuity = [ksc.KEY_MINUS, ksc.KEY_LCONTROL, 2, "Ingenuity"]
inner_quiet = [ksc.KEY_EQUALS, ksc.KEY_LCONTROL, 2, "Inner Quiet"]

macros = {
    "35d 606cp": [
        reflect,
        manipulation,
        ingenuity,
        innovation,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        ingenuity,
        innovation,
        manipulation,
        delicate_synthesis,
        basic_touch,
        basic_touch,
        ingenuity,
        innovation,
        basic_touch,
        great_strides,
        byregots_blessing,
        basic_synthesis,
    ],
    "70d 620cp": [
        reflect,
        ingenuity,
        innovation,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        manipulation,
        ingenuity,
        innovation,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        prudent_touch,
        great_strides,
        ingenuity,
        innovation,
        standard_touch,
        great_strides,
        byregots_blessing,
        careful_synthesis,
    ],
    "35d 538cp": [
        reflect,
        manipulation,
        ingenuity,
        innovation,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        delicate_synthesis,
        ingenuity,
        innovation,
        manipulation,
        delicate_synthesis,
        great_strides,
        byregots_blessing,
        careful_synthesis,
    ]
}