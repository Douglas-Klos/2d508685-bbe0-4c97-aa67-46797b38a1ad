""" A simple FFXIV keyboard based crafting bot """

from ffxiv_2 import *

def send_key(spell):
    if spell[1]:
        PressKey(spell[1])
        time.sleep(.05)

    PressKey(spell[0])
    time.sleep(.05)
    ReleaseKey(spell[0])

    if spell[1]:
        time.sleep(.05)
        ReleaseKey(spell[1])


def craft(rotation, count = 1, collectable = False):
    remaining = count
    while remaining >= 1:
        step = 0
        remaining -= 1

        print(f"Crafting {count - remaining} of {count}")

        for spell in rotation:
            step += 1
            print(f". . . Step {step} of {len(rotation)}: {spell.__name__}")
            SendKey(spell)

        print(f". . . Crafting {count - remaining} of {count} complete!")

        if remaining >= 1:
            time.sleep(3)
            menu_select()
            menu_select()
            menu_select()
            time.sleep(1)


if __name__ == "__main__":
    # time.sleep(2)

    # print(f"Select crafting macro: ")
    for counter, key in enumerate(macros.keys()):
        print(f"{counter}: {key}")

    selection = int(input("Select macro >>> "))
    iterations = int(input("Number to craft >>> "))

    print("Starting in 3 . . .")
    time.sleep(1)
    print("2 . . .")
    time.sleep(1)
    print("1 . . .")
    time.sleep(1)

    rotation = macros[list(macros)[selection]]

    craft(rotation, iterations)



