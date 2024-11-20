import sys
import time

def cool_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def help():
    print("Valid commands: ")
    print("\"help\" - display this help message")
    print("\"move [DIRECTION]\" - move in that direction")
    print("\"interact\" - interact with the area")
    print("\"inventory\" - display your current inventory")
    print("\"inspect [ITEM NAME]\" - inspect an item in your inventory")
    print("\"map\" - display a map of the current room")
    print("\"quit\" - quit the game\n")

# Transitional text for trapdoor event
def cabin_to_forest_transitional_text():
    time.sleep(1)
    cool_print("\nYou open the trapdoor and a cool breeze greets you from below.")
    time.sleep(2)
    cool_print("After a moment's hesitation, you descend into the dark passageway.")
    time.sleep(3)
    cool_print("Emerging on the other side, you find yourself in a dense forest with towering trees around.\n")
    time.sleep(1)

# Flavor text for player waking up
def wake_up_flavor_text():
    time.sleep(1)
    cool_print("\nYou feel groggy, your head throbs slightly as you open your eyes.")
    time.sleep(3)
    cool_print("The faint smell of wood and ash fills the air, and as you sit up, you realize you're in a small, cramped cabin.")
    time.sleep(3)
    cool_print("The dim light filters through cracks in the floorboard above you, casting shadows across the rough wooden walls.")
    time.sleep(3)
    cool_print("You notice a few things around you in this tiny cabin - perhaps you should take a look.\n")
    time.sleep(1)

def ufo_explosion_text():
    time.sleep(1)
    cool_print("\nYou arm the explosive and take off for the treeline, taking cover behind a sturdy tree.")
    time.sleep(2)
    cool_print("As the explosive detonates, the forest around you is engulfed in a blinding flash of light.")
    time.sleep(2)
    cool_print("When you look back, you discover that, as you had hoped, the explosive blew an opening in the structure.")
    time.sleep(2)
    cool_print("You approach the opening and step inside.\n")

def ufo_lit_text():
    time.sleep(1)
    cool_print("\nYou put the battery in the slot.")
    time.sleep(2)
    cool_print("Suddenly, a loud whirring noise emanates from the interior of the ship.")
    time.sleep(2)
    cool_print("Electronics flicker to life, and a bright light fills the room.")