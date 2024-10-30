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
    

def initializeCabin():
    pass

def run_command(player: p.Player, command: str = "exit") -> bool:
    if "move" in command.lower():
        player.move(command)
    elif "inventory" in command.lower():
        player.print_inventory()
    elif "test" in command.lower():
        print("you tested a command")
    elif "help" in command.lower():
        print("We dont have anything here yet :(")
    elif "exit" in command.lower() or "quit" in command.lower():
        return False
    else:
        print("Please enter a valid command!")
    print("")
    return True

myPlayer = p.Player("Jon")
testItem = i.Item("stick", "a desciption")
fakeRealItem = i.Item("bomb", "explode")

starting = True
running = True

title_screen()
while starting:
    start = input("")
    if start == "1" or start.lower() == "new game":
        starting = False
        print("Starting a new game!\n")
    elif start == "2" or start.lower() == "help":
        print("I'm helping!\n")
    elif start == "3" or start.lower() == "quit":
        starting = False
        running = False
        print("Closing the game!\n")

while running:
    cmd = input("Enter a command: ")
    running = run_command(myPlayer, cmd)
