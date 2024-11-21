# Class: Player
# Authors: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney 
# Version 1.0 
# Course: CSE 201 Fall 2024
# Written: November 2024
# Purpose: A class to hold player character, location, and inventory. 

import item as i
import room as r

# A class to hold the player character, location, and inventory
# add access that information for other classes
class Player:
    def __init__(self, name: str, current_room: r.Room, game=None):
        self.player_name = name
        self.item_inventory = []
        self.notes_inventory = []
        self.room_location = (1, 1)  # Player starts at the center tile
        self.current_room = current_room  # Reference to the current room
        self.game = game

    # Sets the player's current room
    # param room: The room the player is moving to
    def set_current_room(self, room):
        self.current_room = room
    
    # Gets the players name
    # Return str: a string of the players name.
    def get_player_name(self) -> str:
        return self.player_name
    
    # Adds an item to the players inventory
    # param item: The item the user is adding to the inventory.
    def add_item(self, item: i.Item):
        self.item_inventory.append(item)

    # Removes item from players inventory.
    # param item: The item the user is trying to remove from inventory.
    # Returns bool: if item is removed from inventory -> true, 
    # o.w -> false.
    def remove_item(self, item: i.Item) -> bool:
        # If item is in inventory
        if item in self.item_inventory:
            self.item_inventory.remove(item)
            return True
        else:
            return False

    # Returns whether player has an item in the inventory or not.
    # param item_name: a string representing the name of the item
    # Return bool: if item is in the inventory -> true, 
    # o.w -> false.
    def has_item(self, item_name: str) -> bool:
        return any(item.get_name() == item_name for item in self.item_inventory)

    # Prints items in the inventory, if empty "Your inventory is empty" will be printed.
    def print_inventory(self):
        # If inventory is empty
        if not self.item_inventory:
            print("Your inventory is empty.")
        # If an item is in the inventory
        else:
            print("You have the following items in your inventory:")
            # Loops through items in the inventory
            for item in self.item_inventory:
                print(f"- {item.get_name()}: {item.get_description()}")
    
    # Inspect an item in the inventory and display its description.
    # param item_name: a string representing the item name.
    def inspect_item(self, item_name: str):
        # Loops through items in inventory
        for item in self.item_inventory:
            if item.get_name().lower() == item_name.lower():
                print(item.get_inspection_text())
                return
        # If the item is not found in inventory
        print(f"You don't have an item named '{item_name}' in your inventory.")

    # Moves the player
    # param direction: A string representing where the player wants to move.
    # return bool: if the player can move in the direction -> true, o.w -> false
    def move(self, direction: str) -> bool:
        text = ""
        alt_text = ""
        # Cabin
        if self.current_room.get_room_name() == "Cabin":
            text = "It's just a wall."
        # Forest
        elif self.current_room.get_room_name() == "Forest":
            text = "A sickly pale fog blocks your path, an unnatural glow emanating from its depths. You move to step into it, but your muscles tense, almost as though your body won't allow you to go any further."
            alt_text = "The dense foliage blocks your path."
        # UFO unlit
        elif self.current_room.get_room_name() == "ufoUnlit":
            text = "It's just a wall."
        # UFO lit
        elif self.current_room.get_room_name() == "ufoLit":
            text = "It's just a wall."
        # Invalid room
        else:
            print("Invalid room or room not recognized.")
            return False

        x, y = self.room_location
        new_x, new_y = x, y  # Default to current position

        # Determine new position based on the direction
        if "left" in direction.lower() or "west" in direction.lower():
            if x > 0:
                new_x -= 1
            else:
                print(text)
                return False
        elif "right" in direction.lower() or "east" in direction.lower():
            if x < self.current_room.size - 1:
                new_x += 1
            else:
                print(text)
                return False
        elif "up" in direction.lower() or "north" in direction.lower():
            if y > 0:
                new_y -= 1
            else:
                print(text)
                return False
        elif "down" in direction.lower() or "south" in direction.lower():
            if y < self.current_room.size - 1:
                new_y += 1
            else:
                print(text)
                return False
        else:
            print("Please enter a valid command!")
            return False
        
        if (new_x, new_y) in self.current_room.areas:
            if self.current_room.areas[(new_x, new_y)] == "X":
                print(alt_text)
                return False
            else:
                # Update position if valid
                self.room_location = (new_x, new_y)
                self.current_room.enter_area(new_x, new_y)  # Enter area only when valid
                return True
        else:
            print(text)
            return False
