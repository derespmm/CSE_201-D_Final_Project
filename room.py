import item as i
import random
import time
import main

pass1 = str(random.randint(10, 99))
pass2 = str(random.randint(10, 99))
password = pass1 + pass2

class Room:
    def __init__(self, room_name: str, room_description, areas, interaction_texts):
        self.room_name = room_name                # Room name
        self.room_description = room_description  # Room description
        self.areas = areas                        # 2D list of areas within the room
        self.size = len(areas)
        self.interactions = interaction_texts     # Size based on the number of rows in areas
        self.boxUnlocked = False

    
    
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
        
    # Returns true if code is correct, false o.w.
    def check_code(self, code):
        if code == password:
            return True
        else:
            return False
    
    # Allows user to interact with specific areas.
    def interact_with_area(self, x, y, player):
        # Interact with the specified tile based on coordinates.
        if (x, y) == (0, 1):
            notebook_name = "notebook"
            if player.has_item(notebook_name):
                print("You already have the tattered notebook. There is nothing more for you to do here.")
            else:
                # Player finds the notebook
                print(self.interactions[(0, 1)])  # Original interaction text
                notebook = i.Item(notebook_name, "An old, fragile notebook filled with faded notes and diagrams.", "You examine the notebook. It says " + pass1 + ".")
                player.add_item(notebook)
                print("You take the tattered notebook and add it to your inventory.")
        elif (x, y) == (2, 1):
            paper_name = "paper"
            if player.has_item(paper_name):
                print("You already have the torn piece of paper. There is nothing more for you to do here.")
            else:
                # Player finds the paper
                print(self.interactions[(2, 1)])  # Original interaction text
                paper = i.Item(paper_name, "A torn piece of paper.", "You examine the torn piece of paper. The numbers " + pass2 + " are barely discernible, scribbled in red ink which has nearly faded.")
                player.add_item(paper)
                print("You take the torn piece of paper and add it to your inventory.")
        elif (x, y) == (1, 2):
            crowbar_name = "crowbar"
            if self.boxUnlocked:
                print("The box is already unlocked. There is nothing more for you to do here.")
            else:
                code = input("Enter the code: ")
                if self.check_code(code):
                    self.boxUnlocked = True
                    crowbar = i.Item(crowbar_name, "A rusty crowbar.")
                    player.add_item(crowbar)
                    print("You unlock the box and add the crowbar to your inventory.")
                else:
                    print("The lock doesn't budge.")
        elif (x, y) == (2, 0):
            if player.has_item("crowbar"):
                quit()
            else:
                print(self.interactions[(2, 0)])
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])  # General interactions for other tiles
        else:
            print("There is nothing to interact with here.")
