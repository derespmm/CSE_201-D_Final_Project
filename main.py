# Python Text RPG
# Names: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold

import cmd
import textwrap
import sys
import os
import time
import timeit
import random
import shutil
import item as i
import player as p
import room as r

terminal_width = shutil.get_terminal_size().columns
width = 50

def title_screen():
    """A title screen wow!"""
    print("+================================================+")
    print(str.center("Welcome to Unearthed Echoes", width))
    print("+================================================+")
    print("1. New Game")
    print("2. Help")
    print("3. Quit\n")

def initialize_cabin():
    """Initializes a 3x3 cabin with descriptions for each area."""
    # Define the 3x3 grid with basic descriptions
    cabin_layout = [
        ["You find yourself in a dusty corner. Theres nothing of interest here.", "You look at the concrete wall in front of you. Theres nothing of interest here.", "A ladder is propped up against the wall, leading to a trapdoor."],
        ["Theres an ordinary bookshelf.", "the center of the cabin", "There's a torn piece of paper."],
        ["You see a shelf hung up, but nothing is on it. Theres nothing of interest here.", "There is a toolbox secured with a 4-digit padlock", "A spider is crawling on the floor. There is nothing of interest here."],
    ]
    cabin = r.Room("Cabin", "A dimly lit, cramped cabin.", cabin_layout)
    return cabin

def wake_up_flavor_text():
    """Flavor text for the player waking up in the cabin."""
    time.sleep(1)
    print("\nYou feel groggy, your head throbs slightly as you open your eyes.")
    time.sleep(4)
    print("The faint smell of wood and ash fills the air, and as you sit up, you realize you're in a small, cramped cabin.")
    time.sleep(4)
    print("The dim light filters through cracks in the floorboard above you, casting shadows across the rough wooden walls.")
    time.sleep(4)
    print("You notice a few things around you in this tiny cabin - perhaps you should take a look.\n")

def run_command(player: p.Player, cabin: r.Room, command: str = "exit") -> bool:
    if "move" in command.lower():
        direction = command.split(" ", 1)[1] if len(command.split()) > 1 else ""
        player.move(direction, cabin)
    elif "inventory" in command.lower():
        player.print_inventory()
    elif "test" in command.lower():
        print("You tested a command")
    elif "help" in command.lower():
        print("Try moving around with commands like 'move left', 'move up'.")
    elif "exit" in command.lower() or "quit" in command.lower():
        return False
    else:
        print("Please enter a valid command!")
    print("")
    return True

# Game initialization
myPlayer = p.Player("Jon")
testItem = i.Item("stick", "a rough, wooden stick")
fakeRealItem = i.Item("bomb", "a small, black spherical object")

starting = True
running = True

title_screen()
while starting:
    start = input("")
    if start == "1" or start.lower() == "new game":
        starting = False
        print("Starting a new game!\n")
        wake_up_flavor_text()
        cabin = initialize_cabin()
        myPlayer.room_location = (1, 1)  # Center of the 3x3 cabin grid
    elif start == "2" or start.lower() == "help":
        print("I'm helping!\n")
    elif start == "3" or start.lower() == "quit":
        starting = False
        running = False
        print("Closing the game!\n")

while running:
    cmd = input("Enter a command: ")
    running = run_command(myPlayer, cabin, cmd)
