# Python Text RPG
# Names: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney
# Version 1.0

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

# Initialize game with settings and player. 
class Game:
    def __init__(self):
        self.cabin = self.initialize_cabin()
        self.player = p.Player("Jon", current_room=self.cabin)
        self.running = True
    
    # Prints the title screen
    def title_screen(self):
        """A title screen wow!"""
        print("+================================================+")
        print(str.center("Welcome to Unearthed Echoes", width))
        print("+================================================+")
        print("1. New Game")
        print("2. Help")
        print("3. Quit\n")

    def initialize_cabin(self):
        # Initializes a 3x3 cabin with descriptions for each area.
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

    # Flavor text for the player waking up in the cabin.
    def wake_up_flavor_text(self):
        time.sleep(1)
        print("\nYou feel groggy, your head throbs slightly as you open your eyes.")
        time.sleep(3)
        print("The faint smell of wood and ash fills the air, and as you sit up, you realize you're in a small, cramped cabin.")
        time.sleep(3)
        print("The dim light filters through cracks in the floorboard above you, casting shadows across the rough wooden walls.")
        time.sleep(3)
        print("You notice a few things around you in this tiny cabin - perhaps you should take a look.\n")
        time.sleep(1)

    # Processes player commands and implement actions. 
    def run_command(self, command: str = "exit") -> bool:
        if "move" in command.lower():
            self.player.move(command)
        elif "inventory" in command.lower():
            self.player.print_inventory()
        elif "test" in command.lower():
            print("you tested a command")
        elif "inspect" in command.lower() or "examine" in command.lower():
            item_name = command.split(" ", 1)[1] if " " in command else ""
            self.player.inspect_item(item_name)
        elif "interact" in command.lower():
            x, y = self.player.room_location  # Get player's current position
            if self.player.current_room:
                self.player.current_room.interact_with_area(x, y, self.player)
            else:
                print("There is no room to interact with.")
        elif "help" in command.lower():
            print("Valid commands: ")
            print("\"help\" - display this help message")
            print("\"move [DIRECTION]\" - move in that direction")
            print("\"interact\" - interact with the area")
            print("\"inventory\" - display your current inventory")
            print("\"inspect [ITEM_NAME]\" - inspect an item in your inventory")
            print("\"quit\" - quit the game")
        elif "exit" in command.lower() or "quit" in command.lower():
            return False
        else:
            print("Please enter a valid command!")
        print("")
        return True

    # Starts the game, displays title screen, and handles inputs from player. 
    def start(self):
        self.title_screen()
        starting = True
        while starting:
            start = input("")
            if start == "1" or start.lower() == "new game":
                starting = False
                print("Starting a new game!")
                self.wake_up_flavor_text()
                self.player.room_location = (1, 1)  # Center of the 3x3 cabin grid
            elif start == "2" or start.lower() == "help":
                print("Valid commands: ")
                print("\"help\" - display this help message")
                print("\"move [DIRECTION]\" - move in that direction")
                print("\"interact\" - interact with the area")
                print("\"inventory\" - display your current inventory")
                print("\"inspect [ITEM_NAME]\" - inspect an item in your inventory")
                print("\"quit\" - quit the game")
            elif start == "3" or start.lower() == "quit":
                starting = False
                self.running = False
                print("Closing the game!\n")

        while self.running:
            cmd = input("Enter a command: ")
            self.running = self.run_command(cmd)

# Game initialization
if __name__ == "__main__":
    game = Game()
    game.start()
