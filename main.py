# Python Text RPG
# Class: Main 
# Authors: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney 
# Version 1.0 
# Course: CSE 201 Fall 2024
# Written: November 2024
# Purpose: 

# main.py
import shutil
import player as p
import room as r
try:
    import pygame
except ImportError:
    pygame = None
from utils import *
from game_map import GameMap

terminal_width = shutil.get_terminal_size().columns
width = 50

# Initialize game with settings and player
class Game:

    def __init__(self):
        self.game_map = GameMap()
        self.cabin = self.initialize_cabin()
        self.forest = self.initialize_forest()
        self.ufoUnlit = self.initialize_ufoUnlit()
        self.ufoLit = self.initialize_ufoLit()
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
    
    def initialize_ufoUnlit(self):
        ufoUnlit_layout = {}
        interaction_texts = {}
        with open("ufoInfoUnlit.txt", "r") as ufoInfoUnlit:
            ufoInfoUnlit.readline()
            for x in range(3):
                for y in range(3):
                    ufoUnlit_layout[(x, y)] = ufoInfoUnlit.readline().strip()
            ufoInfoUnlit.readline()
            ufoInfoUnlit.readline()
            for x in range(3):
                for y in range(3):
                    interaction_texts[(x, y)] = ufoInfoUnlit.readline().strip()
            ufoInfoUnlit.readline()
        return r.Room("ufoUnlit", "Description", ufoUnlit_layout, interaction_texts)
    
    def initialize_ufoLit(self):
        ufoLit_layout = {}
        interaction_texts = {}
        with open("ufoInfoLit.txt", "r") as ufoInfoLit:
            ufoInfoLit.readline()
            for x in range(3):
                for y in range(3):
                    ufoLit_layout[(x, y)] = ufoInfoLit.readline().strip()
            ufoInfoLit.readline()
            ufoInfoLit.readline()
            for x in range(3):
                for y in range(3):
                    interaction_texts[(x, y)] = ufoInfoLit.readline().strip()
            ufoInfoLit.readline()
        return r.Room("ufoLit", "Description", ufoLit_layout, interaction_texts)

    # Updates to handle player commands including room transition
    def run_command(self, command: str = "exit") -> bool:
        if "move" in command.lower():
            if self.player.move(command):
                self.game_map.mark_explored(
                    self.player.current_room.get_room_name(),
                    self.player.room_location
                )
                self.game_map.draw_room(
                    self.player.current_room.get_room_name(),
                    self.player.room_location,
                    self.player.current_room.areas
                )
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
        elif "map" in command.lower():
            self.player.current_room.map(self.player)
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
            if start == "1" or "new game" in start.lower():
                starting = False
                print("Starting a new game!")
                wake_up_flavor_text()
                self.player.room_location = (1, 1)
                self.game_map.mark_explored(self.player.current_room.get_room_name(), (1, 1))
                self.game_map.draw_room(
                    self.player.current_room.get_room_name(),
                    self.player.room_location,
                    self.player.current_room.areas
                )
            elif start == "2" or "help" in start.lower():
                help()
            elif start == "3" or "quit" in start.lower():
                starting = False
                self.running = False
                print("Closing the game!\n")
            elif start == "4" or "debug" in start.lower():
                starting = self.debug_mode()
            else:
                print("Please enter a valid command!\n")

        while self.running:
            if not self.game_map.handle_events():
                self.running = False
                break
                    
            cmd = input("Enter a command: ")
            self.running = self.run_command(cmd)
    
        self.game_map.close()


    def debug_mode(self):
        print("[ENTERING SUPER HACKER DEBUG MODE!!!]")
        location = input("What room do you want to start in? ")
        if "cabin" in location.lower():
            print("Now you're in the cabin at 1,1\n")
            self.player.current_room = self.cabin
            self.player.room_location = (1, 1)
            return False
        elif "forest" in location.lower():
            r.forestUnlocked = True
            self.player.current_room = self.forest
            self.player.room_location = (2, 3)
            print("Now you're in the forest at 2,3\n")
            return False
        elif ("ufo unlit") in location.lower():
            r.forestUnlocked = True
            r.ufoUnlocked = True
            self.player.current_room = self.ufoUnlit
            self.player.room_location = (1, 2)
            print("Now you're in the ufo unlit at 1,2\n")
            return False
        elif ("ufo lit") in location.lower():
            r.forestUnlocked = True
            r.ufoUnlocked = True
            r.ufoLit = True
            self.player.current_room = self.ufoLit
            self.player.room_location = (1, 2)
            print("you're in the ufo lit at 1,2\n")
            return False
        else:
            print("Incorrect input now leaving suepr hack debug moer\n")
            return True


# Game initialization
if __name__ == "__main__":
    game = Game()
    game.start()
