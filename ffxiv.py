import keyboard_scan_codes as ksc
from send_key import *

### Final Fantasy 14 Crafting functions

# General


def menu_select():
    # print(". . . menu select")
    SendKey(ksc.KEY_NUMPAD0)
    time.sleep(0.1)


# Hotbar 1


def muscle_memory():
    # print(". . . muscle memory")
    SendKey(ksc.KEY_1)
    time.sleep(3)


def rapid_synthesis():
    # print(". . . rapid synthesis")
    SendKey(ksc.KEY_2)
    time.sleep(3)


def basic_synthesis():
    # print(". . . rapid synthesis")
    SendKey(ksc.KEY_3)
    time.sleep(3)


def careful_synthesis():
    # print(". . . careful synthesis")
    SendKey(ksc.KEY_4)
    time.sleep(3)


def delicate_synthesis():
    # print(". . . delicate synthesis")
    SendKey(ksc.KEY_5)
    time.sleep(3)


def reuse():
    # print(". . . reuse")
    SendKey(ksc.KEY_6)
    time.sleep(2)


def hasty_touch():
    # print(". . . hasty touch")
    SendKey(ksc.KEY_7)
    time.sleep(3)


def basic_touch():
    # print(". . . basic touch")
    SendKey(ksc.KEY_8)
    time.sleep(3)


def standard_touch():
    # print(". . . standard touch")
    SendKey(ksc.KEY_9)
    time.sleep(3)


def preperatory_touch():
    # print(". . . preperatory touch")
    SendKey(ksc.KEY_0)
    time.sleep(3)


def patient_touch():
    # print(". . . patient touch")
    SendKey(ksc.KEY_MINUS)
    time.sleep(3)


def collectable_synthesis():
    # print(". . . collectable synthesis")
    SendKey(ksc.KEY_EQUALS)
    time.sleep(2)


# Hotbar 2


def name_of_the_elements():
    # print(". . . name of the elements")
    SendKey(ksc.KEY_1, ksc.KEY_LSHIFT)
    time.sleep(2)


def brand_of_the_elements():
    # print(". . . brand of the elements")
    SendKey(ksc.KEY_2, ksc.KEY_LSHIFT)
    time.sleep(3)


def intensive_synthesis():
    # print(". . . intensive synthesis")
    SendKey(ksc.KEY_3, ksc.KEY_LSHIFT)
    time.sleep(3)


def focused_synthesis():
    # print(". . . focused synthesis")
    SendKey(ksc.KEY_5, ksc.KEY_LSHIFT)
    time.sleep(3)


def observe():
    # print(". . . observe")
    SendKey(ksc.KEY_6, ksc.KEY_LSHIFT)
    time.sleep(2)


def focused_touch():
    # print(". . . focused touch")
    SendKey(ksc.KEY_7, ksc.KEY_LSHIFT)
    time.sleep(3)


def precise_touch():
    # print(". . . precise touch")
    SendKey(ksc.KEY_8, ksc.KEY_LSHIFT)
    time.sleep(3)


def prudent_touch():
    # print(". . . prudent touch")
    SendKey(ksc.KEY_9, ksc.KEY_LSHIFT)
    time.sleep(3)


def byregots_blessing():
    # print(". . . byregot's blessing")
    SendKey(ksc.KEY_0, ksc.KEY_LSHIFT)
    time.sleep(3)


def trained_eye():
    # print(". . . trained eye")
    SendKey(ksc.KEY_EQUALS, ksc.KEY_LSHIFT)
    time.sleep(3)


# Hotbar 3


def masters_mend():
    # print(". . . masters mend")
    SendKey(ksc.KEY_1, ksc.KEY_LCONTROL)
    time.sleep(2)


def final_apprasial():
    # print(". . . final apprasial")
    SendKey(ksc.KEY_2, ksc.KEY_LCONTROL)
    time.sleep(2)


def waste_not():
    # print(". . . waste not")
    SendKey(ksc.KEY_3, ksc.KEY_LCONTROL)
    time.sleep(2)


def wate_not_2():
    # print(". . . waste not 2")
    SendKey(ksc.KEY_4, ksc.KEY_LCONTROL)
    time.sleep(2)


def manipulation():
    # print(". . . manipulation")
    SendKey(ksc.KEY_5, ksc.KEY_LCONTROL)
    time.sleep(2)


def tricks_of_the_trade():
    # print(". . . tricks of the trade")
    SendKey(ksc.KEY_7, ksc.KEY_LCONTROL)
    time.sleep(2)


def great_strides():
    # print(". . . great strides")
    SendKey(ksc.KEY_8, ksc.KEY_LCONTROL)
    time.sleep(2)


def innovation():
    # print(". . . innovation")
    SendKey(ksc.KEY_9, ksc.KEY_LCONTROL)
    time.sleep(2)


def reflect():
    # print(". . . reflect")
    SendKey(ksc.KEY_0, ksc.KEY_LCONTROL)
    time.sleep(3)


def ingenuity():
    # print(". . . ingenuity")
    SendKey(ksc.KEY_MINUS, ksc.KEY_LCONTROL)
    time.sleep(2)


def inner_quiet():
    # print(". . . inner quiet")
    SendKey(ksc.KEY_EQUALS, ksc.KEY_LCONTROL)
    time.sleep(2)

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
