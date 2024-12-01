# Class: Item
# Authors: Matt DeRespinis, Teddy Simpson, Dylan Kendall, Noah Arnold, Natalie Taylor, Nolan Burney 
# Version 1.0 
# Course: CSE 201 Fall 2024
# Written: November 2024
# Purpose: A class to hold data for items. 

class Item:
   
    # Creates an item object with a name, description, and inspection text
    # param name: a string containing the name of the item.
    # param description: a string containing the item description.
    # param inspection_text: a string containing text when the player finds the item.
    def __init__(self, name: str, description: str, inspection_text: str = None):
        self.name = name
        self.description = description
        self.inspection_text = inspection_text or description  # Default to description if none provided
        
    # Method to get the name
    # Return str: a string representing the name of item. 
    def get_name(self) -> str:
        return self.name
    
    # Gets the description
    # Return str: a string representing the description of the item.
    def get_description(self) -> str:
        return self.description
    
    # Gets the text when inspecting an item.
    # Return str: a string with the inspection text of the item. 
    def get_inspection_text(self) -> str:
        return self.inspection_text
    
    # Prints the name of item used 
    def use_item(self):
        print("You used the", self.name + "!")
