class Room:
    def __init__(self, room_name, room_description, areas):
        self.room_name = room_name                # Room name
        self.room_description = room_description  # Room description
        self.areas = areas                        # 2D list of areas within the room
        self.size = len(areas)                    # Size based on the number of rows in areas

    # Method to get the room name
    def get_room_name(self):
        return self.room_name

    # Method to get the room description
    def get_room_description(self):
        return self.room_description

    # Simulates moving to a different room (returns True if successful)
    def go_to_room(self):
        # Placeholder for actual logic
        print(f"Going to {self.room_name}")
        return True

    # Simulates entering an area within the room (returns True if successful)
    def enter_area(self, x, y):
        # Check if the given coordinates are within bounds
        if 0 <= x < self.size and 0 <= y < len(self.areas[x]):
            print(f"Entering area at ({x}, {y}): {self.areas[x][y]}")
            return True
        else:
            print("Invalid area coordinates.")
            return False

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