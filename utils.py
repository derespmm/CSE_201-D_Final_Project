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
    print("\"inspect [ITEM_NAME]\" - inspect an item in your inventory")
    print("\"quit\" - quit the game\n")