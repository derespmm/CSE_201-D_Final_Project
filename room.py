import item as i

class Room:
    def __init__(self, room_name, room_description, areas, interaction_texts):
        self.room_name = room_name                # Room name
        self.room_description = room_description  # Room description
        self.areas = areas                        # 2D list of areas within the room
        self.size = len(areas)         
        self.interactions = interaction_texts           # Size based on the number of rows in areas

    def get_room_name(self):
        return self.room_name

    def get_room_description(self):
        return self.room_description

    def go_to_room(self):
        print(f"Going to {self.room_name}")
        return True

    def enter_area(self, x, y):
    # Check if the given coordinates are within bounds
        if 0 <= x < self.size and 0 <= y < len(self.areas[x]):
            print(f"Entering area at ({x}, {y}): {self.areas[x][y]}")
            return True
        else:
            print("Invalid area coordinates.")
            return False

    def interact_with_area(self, x, y, player):
        """Interact with the specified tile based on coordinates."""
        if (x, y) == (1, 0):
            notebook_name = "notebook"
            if player.has_item(notebook_name):
                print("You already have the tattered notebook. There is nothing more for you to do here.")
            else:
                # Player finds the notebook
                print(self.interactions[(1, 0)])  # Original interaction text
                notebook = i.Item(notebook_name, "An old, fragile notebook filled with faded notes and diagrams.", "ADD FLAVOR TEXT TO FIND THE FIRST 2 DIGITS")
                player.add_item(notebook)
                print("You take the tattered notebook and add it to your inventory.")
        elif (x, y) == (1, 2):
            paper_name = "paper"
            if player.has_item(paper_name):
                print("You already have the torn piece of paper. There is nothing more for you to do here.")
            else:
                # Player finds the paper
                print(self.interactions[(1, 2)])  # Original interaction text
                paper = i.Item(paper_name, "A torn piece of paper.", "You examine the torn piece of paper. The numbers 2 and 4 are barely discernible, scribbled in red ink which has nearly faded.")
                player.add_item(paper)
                print("You take the torn piece of paper and add it to your inventory.")
        elif (x, y) in self.interactions:
            print(self.interactions[(x, y)])  # General interactions for other tiles
        else:
            print("There is nothing to interact with here.")

class Area(Room):
    def __init__(self, room_name, room_description, areas, area_name, area_description, interactables):
        # Initialize Room attributes
        super().__init__(room_name, room_description, areas)
        self.area_name = area_name                   # Area name
        self.area_description = area_description     # Area description
        self.interactables = interactables           # List or dictionary of interactable objects in the area

    def get_area_name(self):
        return self.area_name

    def get_area_description(self):
        return self.area_description

    def go_to_area(self):
        print(f"Going to area: {self.area_name}")
        return True