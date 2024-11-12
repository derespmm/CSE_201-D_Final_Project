# Python Text RPG
# Names: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney
# Version 1.0

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

terminal_width = shutil.get_terminal_size().columns
width = 50

# Initialize game with settings and player. 
class Game:
    def __init__(self):
        self.cabin = self.initialize_cabin()
        self.forest = self.initialize_forest()
        self.player = p.Player("Jon", current_room=self.cabin)
        self.running = True
    
    # Prints the title screen
    def title_screen(self):
        print("+================================================+")
        print(str.center("Welcome to Unearthed Echoes", width))
        print("+================================================+")
        print("1. New Game")
        print("2. Help")
        print("3. Quit\n")

    def initialize_cabin(self):
        # Initialize cabin layout and interaction texts from file
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
    
    def initialize_forest(self):
        # Initialize forest layout and interaction texts from file
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

    # Transitional text for trapdoor event
    def cabin_to_forest_transitional_text(self):
        print("\nYou open the trapdoor and a cool breeze greets you from below.")
        time.sleep(2)
        print("After a moment's hesitation, you descend into the dark passageway.")
        time.sleep(3)
        print("Emerging on the other side, you find yourself in a dense forest with towering trees around.\n")
        time.sleep(1)

    # Flavor text for player waking up
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
            x, y = self.player.room_location
            if self.player.current_room:
                # Check if interaction requires transition
                if self.player.current_room.room_name == "Cabin" and (x, y) == (2, 0):
                    if self.player.has_item("crowbar"):
                        self.cabin_to_forest_transitional_text()
                        self.player.set_current_room(self.forest)
                        self.player.room_location = (2, 3)  # Center of the 5x5 forest grid
                    else:
                        print("The trapdoor is stuck. Maybe there's something to pry it open.")
                else:
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
                print("Valid commands: ")
                print("\"help\" - display this help message")
                print("\"move [DIRECTION]\" - move in that direction")
                print("\"interact\" - interact with the area")
                print("\"inventory\" - display your current inventory")
                print("\"inspect [ITEM NAME]\" - inspect an item in your inventory")
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
