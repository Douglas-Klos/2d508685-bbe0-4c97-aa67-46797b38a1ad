import keyboard_scan_codes as ksc
from send_key import *

# General
menu_select = [ksc.KEY_NUMPAD0, None, .1]

# Crafting Spells
# Key, Modifier, Delay
muscle_memory = [ksc.KEY_1, None, 3]
rapid_synthesis = [ksc.KEY_2, None, 3]
basic_synthesis = [ksc.KEY_3, None, 3]
careful_synthesis = [ksc.KEY_4, None, 3]
delicate_synthesis = [ksc.KEY_5, None, 3]
reuse = [ksc.KEY_6, None, 3]
hasty_touch = [ksc.KEY_7, None, 3]
basic_touch = [ksc.KEY_8, None, 3]
standard_touch = [ksc.KEY_9, None, 3]
preperatory_touch = [ksc.KEY_0, None, 3]
patient_touch = [ksc.KEY_MINUS, None, 3]
collectable_synthesis = [ksc.KEY_EQUALS, None, 2]

name_of_the_elements = [ksc.KEY_1, ksc.KEY_LSHIFT, 2]
brand_of_the_elements = [ksc.KEY_2, ksc.KEY_LSHIFT, 3]
intensive_synthesis = [ksc.KEY_3, ksc.KEY_LSHIFT, 3]
focused_synthesis = [ksc.KEY_5, ksc.KEY_LSHIFT, 2]
observe = [ksc.KEY_6, ksc.KEY_LSHIFT, 3]
focused_touch = [ksc.KEY_7, ksc.KEY_LSHIFT, 3]
precise_touch = [ksc.KEY_8, ksc.KEY_LSHIFT, 3]
prudent_touch = [ksc.KEY_9, ksc.KEY_LSHIFT, 3]
byregots_blessing = [ksc.KEY_0, ksc.KEY_LSHIFT, 3]
trained_eye = [ksc.KEY_EQUALS, KEY_LSHIFT, 3]

masters_mend = [ksc.KEY_1, ksc.KEY_LCONTROL, 2]
final_apprasial = [ksc.KEY_2, ksc.KEY_LCONTROL, 2]
waste_not = [ksc.KEY_3, ksc.KEY_LCONTROL, 2]
waste_not_2 = [ksc.KEY_4, ksc.KEY_LCONTROL, 2]
manipulation = [ksc.KEY_5, ksc.KEY_LCONTROL, 2]
careful_observation = [ksc.KEY_6, ksc.KEY_LCONTROL, 2]
tricks_of_the_trade = [ksc.KEY_7, ksc.KEY_LCONTROL, 3]
great_strides = [ksc.KEY_8, ksc.KEY_LCONTROL, 2]
innovation = [ksc.KEY_9, ksc.KEY_LCONTROL, 2]
reflect = [ksc.KEY_0, ksc.KEY_LCONTROL, 3]
ingenuity = [ksc.KEY_MINUS, KEY_LCONTROL, 2]
inner_quiet = [ksc.KEY_EQUALS, KEY_LCONTROL, 2]

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