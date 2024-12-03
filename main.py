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
import os
try:
    import pygame
except ImportError:
    pygame = None
from utils import *
from game_map import GameMap

terminal_width = shutil.get_terminal_size().columns
width = 50

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize game with settings and player
class Game:

    def __init__(self):
        """
        Initialize the Game class with default settings, including the game map,
        rooms (cabin, forest, ufoUnlit, ufoLit), a player instance named "Jon",
        and set the game running state to True.
        """
        self.game_map = GameMap()
        self.cabin = self.initialize_cabin()
        self.forest = self.initialize_forest()
        self.ufoUnlit = self.initialize_ufoUnlit()
        self.ufoLit = self.initialize_ufoLit()
        self.player = p.Player("Jon", current_room=self.cabin, game=self)
        self.running = True
    
    # Prints the title screen
    def title_screen(self):
        """
        Prints the title screen of Unearthed Echoes.

        The title screen displays the game title, "Unearthed Echoes", centered
        within a border of "=" characters. Below the title, it displays a list of
        options for the user to select: "New Game", "Help", and "Quit".

        :return: None
        """
        print("+================================================+")
        print(str.center("Welcome to Unearthed Echoes", width))
        print("+================================================+")
        print("1. New Game")
        print("2. Help")
        print("3. Quit\n")

    # Initialize cabin layout and interaction texts from file

    def initialize_cabin(self):
        """
        Initialize the cabin room by reading its layout and interaction texts from a file.

        This function reads data from "cabinInfo.txt" to set up the cabin's layout and
        interaction texts. The file is expected to have a specific format where the first
        section represents the cabin layout and the second section contains the interaction
        texts. Each section is read into a dictionary with coordinates as keys.

        :return: A Room object representing the cabin with its layout and interactions.
        """
        cabin_layout = {}
        interaction_texts = {}
        file_path = os.path.join(SCRIPT_DIR, "cabinInfo.txt")
        
        with open(file_path, "r") as cabinInfo:
            # Skip the "# cabin_layout" line
            cabinInfo.readline()
            
            # Read the layout section
            for x in range(3):
                for y in range(3):
                    cabin_layout[(x, y)] = cabinInfo.readline().strip()
                    
            # Skip the blank line and "# interaction_texts" line
            cabinInfo.readline()
            cabinInfo.readline()
            
            # Read the interaction texts
            for x in range(3):
                for y in range(3):
                    interaction_texts[(x, y)] = cabinInfo.readline().strip()
                    
        return r.Room("Cabin", "A dimly lit, cramped cabin.", cabin_layout, interaction_texts, self.game_map)

    def initialize_forest(self):
        """
        Initialize the forest room by reading its layout and interaction texts from a file.

        This function reads data from "forestInfo.txt" to set up the forest's layout and
        interaction texts. The file is expected to have a specific format where the first
        section represents the forest layout and the second section contains the interaction
        texts. Each section is read into a dictionary with coordinates as keys.

        :return: A Room object representing the forest with its layout and interactions.
        """
        forest_layout = {}
        interaction_texts = {}
        file_path = os.path.join(SCRIPT_DIR, "forestInfo.txt")
        
        with open(file_path, "r") as forestInfo:
            # Skip the "# forest_layout" line
            forestInfo.readline()
            
            # Read the layout section
            for x in range(5):
                for y in range(5):
                    forest_layout[(x, y)] = forestInfo.readline().strip()
                    
            # Skip the blank line and "# interaction_texts" line
            forestInfo.readline()
            forestInfo.readline()
            
            # Read the interaction texts
            for x in range(5):
                for y in range(5):
                    interaction_texts[(x, y)] = forestInfo.readline().strip()
                    
        return r.Room("Forest", "A dark and foreboding forest.", forest_layout, interaction_texts, self.game_map)

    def initialize_ufoUnlit(self):
        """
        Initialize the unlit UFO room by reading its layout and interaction texts from a file.

        This function reads data from "ufoInfoUnlit.txt" to set up the unlit UFO's layout and
        interaction texts. The file is expected to have a specific format where the first
        section represents the UFO layout and the second section contains the interaction
        texts. Each section is read into a dictionary with coordinates as keys.

        :return: A Room object representing the unlit UFO with its layout and interactions.
        """
        ufoUnlit_layout = {}
        interaction_texts = {}
        file_path = os.path.join(SCRIPT_DIR, "ufoInfoUnlit.txt")
        
        with open(file_path, "r") as ufoInfoUnlit:
            # Skip the "# ufo_unlit_layout" line
            ufoInfoUnlit.readline()
            
            # Read the layout section
            for x in range(3):
                for y in range(3):
                    ufoUnlit_layout[(x, y)] = ufoInfoUnlit.readline().strip()
                    
            # Skip the blank line and "# interaction_texts" line
            ufoInfoUnlit.readline()
            ufoInfoUnlit.readline()
            
            # Read the interaction texts
            for x in range(3):
                for y in range(3):
                    interaction_texts[(x, y)] = ufoInfoUnlit.readline().strip()
                    
        return r.Room("ufoUnlit", "A dark, mysterious structure.", ufoUnlit_layout, interaction_texts, self.game_map)

    def initialize_ufoLit(self):
        """
        Initialize the lit UFO room by reading its layout and interaction texts from a file.

        This function reads data from "ufoInfoLit.txt" to set up the lit UFO's layout and
        interaction texts. The file is expected to have a specific format where the first
        section represents the UFO layout and the second section contains the interaction
        texts. Each section is read into a dictionary with coordinates as keys.

        :return: A Room object representing the lit UFO with its layout and interactions.
        """
        ufoLit_layout = {}
        interaction_texts = {}
        file_path = os.path.join(SCRIPT_DIR, "ufoInfoLit.txt")
        
        with open(file_path, "r") as ufoInfoLit:
            # Skip the "# ufo_lit_layout" line
            ufoInfoLit.readline()
            
            # Read the layout section
            for x in range(3):
                for y in range(3):
                    ufoLit_layout[(x, y)] = ufoInfoLit.readline().strip()
                    
            # Skip the blank line and "# interaction_texts" line
            ufoInfoLit.readline()
            ufoInfoLit.readline()
            
            # Read the interaction texts
            for x in range(3):
                for y in range(3):
                    interaction_texts[(x, y)] = ufoInfoLit.readline().strip()
                    
        return r.Room("ufoLit", "An illuminated alien structure.", ufoLit_layout, interaction_texts, self.game_map)

    # Updates to handle player commands including room transition
    def run_command(self, command: str = "exit") -> bool:
        """
        Run a command for the player.

        This function takes a command string, and performs the action associated with the
        command. The player's current room and location are taken into account when
        performing the action.

        :param command: The command string to run.
        :return: True if the game should continue, False if the game should exit.
        """
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

                # To make the map update upon switching rooms
                self.game_map.draw_room(
                    self.player.current_room.get_room_name(),
                    self.player.room_location,
                    self.player.current_room.areas
                )

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
        """
        The game starting screen and initializes all neeeded objects.

        This function starts the game and contains the main game loop. It first displays the
        title screen, then waits for the user to enter a command. If the command is "new game",
        the user is placed in the starting room. If the command is "help", the help function is
        called. If the command is "quit", the game exits. If the command is "debug", the debug
        mode is entered. If the command is anything else, the user is asked to enter a valid
        command.

        Once the game is running, the user can enter commands to move around, interact with
        objects, inspect items, and so on. The game continues to run until the user enters
        "quit" or closes the window.
        """
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
        """
        Allows the user to enter debug mode, which allows them to select a room
        to start in. The user can enter "cabin", "forest", "ufo unlit", or "ufo lit" to enter
        the respective room. The user will be placed at the location (1,1) in the cabin, (2,3)
        in the forest, (1,2) in the ufo unlit, or (1,2) in the ufo lit. The corresponding
        room's areas will be marked as explored and drawn on the map. If the user enters
        anything else, the function will return True, indicating that super hack debug mode
        should not be exited. If the user enters a valid room name, the function will return
        False, indicating that debug mode should be exited.
        """
        print("[ENTERING SUPER HACKER DEBUG MODE!!!]")
        location = input("What room do you want to start in? ")
        if "cabin" in location.lower():
            print("You're in the cabin at 1,1\n")
            self.player.current_room = self.cabin
            self.player.room_location = (1, 1)
            self.game_map.mark_explored(
                self.player.current_room.get_room_name(),
                self.player.room_location
            )
            self.game_map.draw_room(
                self.player.current_room.get_room_name(),
                self.player.room_location,
                self.player.current_room.areas
            )
            return False
        elif "forest" in location.lower():
            r.forestUnlocked = True
            self.player.current_room = self.forest
            self.player.room_location = (2, 3)
            self.game_map.mark_explored(
                self.player.current_room.get_room_name(),
                self.player.room_location
            )
            self.game_map.draw_room(
                self.player.current_room.get_room_name(),
                self.player.room_location,
                self.player.current_room.areas
            )
            print("You're in the forest at 2,3\n")
            return False
        elif ("ufo unlit") in location.lower():
            r.forestUnlocked = True
            r.ufoUnlocked = True
            self.player.current_room = self.ufoUnlit
            self.player.room_location = (1, 2)
            self.game_map.mark_explored(
                self.player.current_room.get_room_name(),
                self.player.room_location
            )
            self.game_map.draw_room(
                self.player.current_room.get_room_name(),
                self.player.room_location,
                self.player.current_room.areas
            )
            print("Now you're in the ufo unlit at 1,2\n")
            return False
        elif ("ufo lit") in location.lower():
            r.forestUnlocked = True
            r.ufoUnlocked = True
            r.ufoLit = True
            self.player.current_room = self.ufoLit
            self.player.room_location = (1, 2)
            self.game_map.mark_explored(
                self.player.current_room.get_room_name(),
                self.player.room_location
            )
            self.game_map.draw_room(
                self.player.current_room.get_room_name(),
                self.player.room_location,
                self.player.current_room.areas
            )
            print("You're in the lit ufo at 1,2\n")
            return False
        else:
            print("Incorrect input now leaving super hack debug mode\n")
            return True


# Game initialization
if __name__ == "__main__":
    game = Game()
    game.start()
