# Python Text RPG
# Class: Main 
# Authors: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney 
# Version 1.0 
# Course: CSE 201 Fall 2024
# Written: November 2024
# Purpose: 

# main.py
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
from utils import cool_print, help

terminal_width = shutil.get_terminal_size().columns
width = 50

# Initialize game with settings and player
class Game:
    def __init__(self):
        self.cabin = self.initialize_cabin()
        self.forest = self.initialize_forest()
        self.player = p.Player("Jon", current_room=self.cabin, game=self)
        self.running = True
    
    # Prints the title screen
    def title_screen(self):
        print("+================================================+")
        print(str.center("Welcome to Unearthed Echoes", width))
        print("+================================================+")
        print("1. New Game")
        print("2. Help")
        print("3. Quit\n")

    # Initialize cabin layout and interaction texts from file
    def initialize_cabin(self):
        cabin_layout = {}
        interaction_texts = {}
        with open("cabinInfo.txt", "r") as cabinInfo:
            cabinInfo.readline()
            for x in [0, 1, 2]:
                for y in [0, 1, 2]:
                    cabin_layout[(x, y)] = cabinInfo.readline().strip()
            cabinInfo.readline()
            cabinInfo.readline()
            for x in [0, 1, 2]:
                for y in [0, 1, 2]:
                    interaction_texts[(x, y)] = cabinInfo.readline().strip()
            cabinInfo.readline()
        return r.Room("Cabin", "A dimly lit, cramped cabin.", cabin_layout, interaction_texts)
    
    # Initialize forest layout and interaction texts from file
    def initialize_forest(self):
        forest_layout = {}
        interaction_texts = {}
        with open("forestInfo.txt", "r") as forestInfo:
            forestInfo.readline()
            for x in range(5):
                for y in range(5):
                    forest_layout[(x, y)] = forestInfo.readline().strip()
            forestInfo.readline()
            forestInfo.readline()
            for x in range(5):
                for y in range(5):
                    interaction_texts[(x, y)] = forestInfo.readline().strip()
            forestInfo.readline()
        return r.Room("Forest", "Description", forest_layout, interaction_texts)

    # Flavor text for player waking up
    def wake_up_flavor_text(self):
        time.sleep(1)
        cool_print("\nYou feel groggy, your head throbs slightly as you open your eyes.")
        time.sleep(3)
        cool_print("The faint smell of wood and ash fills the air, and as you sit up, you realize you're in a small, cramped cabin.")
        time.sleep(3)
        cool_print("The dim light filters through cracks in the floorboard above you, casting shadows across the rough wooden walls.")
        time.sleep(3)
        cool_print("You notice a few things around you in this tiny cabin - perhaps you should take a look.\n")
        time.sleep(1)

    # Updates to handle player commands including room transition
    def run_command(self, command: str = "exit") -> bool:
        if "move" in command.lower():
            self.player.move(command)
        elif "inventory" in command.lower():
            self.player.print_inventory()
        elif "inspect" in command.lower() or "examine" in command.lower():
            item_name = command.split(" ", 1)[1] if " " in command else ""
            self.player.inspect_item(item_name)
        elif "interact" in command.lower():
            if self.player.current_room:
                # Directly call interact_with_area for the player's current room and location
                x, y = self.player.room_location
                self.player.current_room.interact_with_area(x, y, self.player)
            else:
                print("There is no room to interact with.")
        elif "help" in command.lower():
            help()
        elif "exit" in command.lower() or "quit" in command.lower():
            return False
        else:
            print("Please enter a valid command!")
        print("")
        return True

    # The game starting screen and initializes all neeeded objects
    def start(self):
        self.title_screen()
        starting = True
        while starting:
            start = input("")
            if start == "1" or start.lower() == "new game":
                starting = False
                print("Starting a new game!")
                self.wake_up_flavor_text()
                self.player.room_location = (1, 1)
            elif start == "2" or start.lower() == "help":
                help()
            elif start == "3" or start.lower() == "quit" or start.lower() == "exit":
                starting = False
                self.running = False
                print("Closing the game!\n")
            elif start.lower() == "debug":
                print("\n[ENTERING SUPER HACKER DEBUG MODE!!!]")
                location = input("What room do you want to start in? ")
                if "cabin" in location.lower():
                    starting = False
                    print("Now you'r in the cabin at 1,1\n")
                    self.player.current_room = self.cabin
                    self.player.room_location = (1, 1)
                elif "forest" in location.lower():
                    starting = False
                    self.player.current_room = self.forest
                    self.player.room_location = (2, 3)
                    print("How your in the forest at 2,3\n")


        while self.running:
            cmd = input("Enter a command: ")
            self.running = self.run_command(cmd)

# Game initialization
if __name__ == "__main__":
    game = Game()
    game.start()
