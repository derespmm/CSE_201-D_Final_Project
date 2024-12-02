# Class: Room
# Authors: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney 
# Version 1.0 
# Course: CSE 201 Fall 2024
# Written: November 2024
# Purpose: A class to hold data for rooms, areas, descriptions, and interactables. 

import item as i
import random
import math
from utils import *

pass1 = str(random.randint(10, 99))
pass2 = str(random.randint(10, 99))
boxUnlocked = False
forestUnlocked = False
ufoUnlocked = False
ufoLit = False
lever1 = 1
lever2 = 1
lever3 = 1

# A class to hold all data of various rooms, areas, descriptions, and interactable objects
class Room:
    def __init__(self, room_name: str, room_description, areas, interaction_texts, game_map=None):
        self.room_name = room_name                # Room name
        self.room_description = room_description  # Room description
        self.areas = areas                        # 2D list of areas within the room
        self.size = len(areas)
        self.interactions = interaction_texts     # Size based on the number of rows in areas
        self.game_map = game_map

    # Returns the current room
    def get_room_name(self) -> str:
        return self.room_name
 
    # Returns the current room description
    def get_room_description(self) -> str:
        return self.room_description
    
    # Prints the room the player is travelling to
    def go_to_room(self) -> bool:
        print(f"Going to {self.room_name}")
        return True

    # Returns true if coordinate is in bounds, false o.w.
    def enter_area(self, x, y):
        # Check if the given coordinates exist in the layout
        if (x, y) in self.areas:
            print(f"Entering area at ({x}, {y}): {self.areas[(x, y)]}")
            return True
        else:
            print("Invalid area coordinates.")
            return False
    
    # Checks if the box code is correct.
    # Returns true if code is correct, false o.w.
    def check_box_code(self, code):
        password1 = pass1 + pass2
        password2 = pass2 + pass1
        # Checks if password is correct.
        if code == password1 or code == password2:
            return True
        else:
            return False

    # Checks if the machine code is correct.
    # Returns True if code is correct, false o.w.    
    def check_machine_code(self, code):
        password = "253"
        if code == password:
            return True
        else:
            return False
        
    def map(self, player):
        if self.get_room_name() == "ufoUnlit":
            print("It's too dark to see anything around you.")
            return

        # Get the player's current coordinates in the room
        x, y = player.room_location
        
        # Iterate over the room layout and print the map
        print(f"\n{self.room_name} Map:")
        for i in range(int(math.sqrt(self.size))):  # Loop over rows (y-axis)
            row = ""
            for j in range(int(math.sqrt(self.size))):  # Loop over columns (x-axis)
                # Mark the player's position with "H", accessible tiles with "O"
                if (j, i) == (x, y):
                    row += "H  "
                elif player.current_room.areas[(j, i)] == "X":
                    row += "X  "
                else:
                    row += "O  "
            print(row)
        print("\nLegend: ")
        print("H: You Are Here")
        print("O: Accessible Tile")
        print("X: Inaccessible Tile")

    # Allows the player to interact with the x, y coordinate.    
    def interact_with_area(self, x, y, player):
        # If player is in the certain room.
        if self.room_name == "Cabin":
            self.interact_with_area_cabin(x, y, player)
        elif self.room_name == "Forest":
            self.interact_with_area_forest(x, y, player)
        elif self.room_name == "ufoUnlit":
            self.interact_with_area_ufoUnlit(x, y, player)
        elif self.room_name == "ufoLit":
            self.interact_with_area_ufoLit(x, y, player)
    
    # Allows user to interact with specific areas.
    def interact_with_area_cabin(self, x, y, player):
        global boxUnlocked
        global forestUnlocked
        if (x, y) == (0, 1):
            notebook_name = "notebook"
            if player.has_item(notebook_name):
                print("You already have the tattered notebook. There is nothing more for you to do here.")
            else:
                # Player finds the notebook
                print(self.interactions[(0, 1)])
                notebook = i.Item(notebook_name, "An old, fragile notebook filled with faded notes and diagrams.", "You examine the notebook. It has many complex formulas and equations, but you see a giant " + pass1 + " in the center of the page.")
                player.add_item(notebook)
                print("You take the tattered notebook and add it to your inventory.")
                if self.game_map:  # Check if game_map exists before using it
                    self.game_map.mark_item_found("Cabin", (x, y))
        elif (x, y) == (2, 1):
            paper_name = "paper"
            if player.has_item(paper_name):
                print("You already have the torn piece of paper. There is nothing more for you to do here.")
            else:
                # Player finds the paper
                print(self.interactions[(2, 1)])  # Original interaction text
                paper = i.Item(paper_name, "A torn piece of paper with some old math formulas on it.", "You examine the torn piece of paper. The number " + pass2 + " is barely discernible, scribbled in red ink which has nearly faded.")
                player.add_item(paper)
                print("You take the torn piece of paper and add it to your inventory.")
                self.game_map.mark_item_found("Cabin", (x, y))
        elif (x, y) == (1, 2):
            crowbar_name = "crowbar"
            # Box has already been unlocked.
            if boxUnlocked:
                print("The box is already unlocked. There is nothing more for you to do here.")
            # Box needs to be unlocked / code needs entered.
            else:
                print("There is a 4-digit padlock on a closed box.")
                code = input("What would you like to enter? ")
                # Code is correct.
                if self.check_box_code(code):
                    boxUnlocked = True
                    crowbar = i.Item(crowbar_name, "A rusty crowbar, that looks like it has been through a lot.")
                    player.add_item(crowbar)
                    print("You unlock the box and add the crowbar to your inventory.")
                # Wrong code was entered by user.
                else:
                    print("The lock doesn't budge.")
        elif (x, y) == (2, 0):
            if forestUnlocked:
                player.set_current_room(player.game.forest)
                player.room_location = (2, 3)
                print("You go back into the forest.")
            else:
                if player.has_item("crowbar"):
                    cabin_to_forest_transitional_text()
                    player.set_current_room(player.game.forest)  # Assuming player has a reference to the game object
                    player.room_location = (2, 3)
                    forestUnlocked = True
                else:
                    print(self.interactions[(2, 0)])
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])  # General interactions for other tiles
        else:
            print("There is nothing to interact with here.")
    
    # Allows player to interact with x, y coordinates in forest.
    def interact_with_area_forest(self, x, y, player):
        if (x, y) == (0, 3):
            battery_name = "battery"
            # Player already has bettery in inventory.
            if player.has_item(battery_name):
                print("You already have the battery. There is nothing more for you to do here.")
            # Player needs to add battery to inventory.
            else:
                print(self.interactions[(x, y)])
                battery = i.Item(battery_name, "It's a quadruple A battery, it looks fully charged.", "A rare battery that looks full of charge. It almost looks alien in nature.")
                player.add_item(battery)
                print("You take the battery and add it to your inventory.")
                if self.game_map:
                    self.game_map.mark_item_found("Forest", (x, y))
        elif (x, y) == (4, 2):
            explosive_name = "explosive"
            # Player already has explosive in inventory.
            if player.has_item(explosive_name):
                print("You already have the explosive device. There is nothing more for you to do here.")
            # Player needs to add explosive to inventory.
            else:
                print(self.interactions[(x, y)])
                explosive = i.Item(explosive_name, "A very fragile explosive that could go off any time soon.", "A powerful explosive that looks like it could blow a hole in solid metal.")
                player.add_item(explosive)
                print("You take the explosive device and add it to your inventory.")
                if self.game_map:
                    self.game_map.mark_item_found("Forest", (x, y))
        elif (x, y) == (2, 3):
            player.set_current_room(player.game.cabin)  # Switch to the Cabin room
            player.room_location = (2, 0)
            print("You go back into the cabin.")
        elif (x, y) == (2, 0):
            if ufoUnlocked: # Only if UFO is unlocked.
                if ufoLit: # Only if UFO is lit.
                    player.set_current_room(player.game.ufoLit)
                    player.room_location = (1, 2)
                    if self.game_map:
                        self.game_map.mark_explored("ufoLit", (1, 2))
                        self.game_map.draw_room("ufoLit", (1, 2), player.game.ufoLit.areas)
                    print("You step back into the UFO.")
                else: # UFO is NOT lit.
                    player.set_current_room(player.game.ufoUnlit)
                    player.room_location = (1, 2)
                    if self.game_map:
                        self.game_map.mark_explored("ufoUnlit", (1, 2))
                        self.game_map.draw_room("ufoUnlit", (1, 2), player.game.ufoUnlit.areas)
                    print("You step back into the UFO.")
            else:
                # Exploding the UFO to Enter.
                if player.has_item("explosive"):
                    player.remove_item("explosive")
                    ufo_explosion_text()
                    player.set_current_room(player.game.ufoUnlit)
                    player.room_location = (1, 2)
                    ufoUnlocked = True
                else:
                    print(self.interactions[(2, 0)])
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])
        else:
            print("There is nothing to interact with here.")
    
    # Allows player to interact with UFO NOT lit.
    def interact_with_area_ufoUnlit(self, x, y, player):
        if (x, y) == (1, 1):
            # Player lights up the UFO.
            if player.has_item("battery"):
                ufo_lit_text()
                player.set_current_room(player.game.ufoLit)
                player.room_location = (1, 1)
            else:
                print(self.interactions[(1, 1)])
        # Player goes back to forest.
        elif (x, y) == (1, 2):
            player.set_current_room(player.game.forest)
            player.room_location = (2, 0)
            print("You go back into the forest.")
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])
        else:
            print("There is nothing to interact with here.")
    
    # Allows player to interact with lit UFO.
    def interact_with_area_ufoLit(self, x, y, player):
        global lever1
        global lever2
        global lever3
        if (x, y) == (0, 1):
            lever1 = input("Select a setting for the lever (1-5): ")
        elif (x, y) == (1, 0):
            lever2 = input("Select a setting for the lever (1-5): ")
        elif (x, y) == (2, 1):
            lever3 = input("Select a setting for the lever (1-5): ")
        elif (x, y) == (2, 2):
            # Code is correct.
            if self.check_machine_code(str(lever1) + str(lever2) + str(lever3)):
                print("Win")
                quit()
            # Code is wrong.
            else:
                print("The machine doesn't respond.")
        elif (x, y) == (1, 2): # Back to the forest
            player.set_current_room(player.game.forest)
            player.room_location = (2, 0)
            print("You go back into the forest.")
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])
        else:
            print("There is nothing to interact with here.")
