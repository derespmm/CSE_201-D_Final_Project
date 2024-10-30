import item as i

class Player:
    """A class for the player character."""

    def __init__(self, name: str):
        self.player_name = name
        self.item_inventory = []
        self.notes_inventory = []
        self.room_location = (1, 1)  # Start in the center of the 3x3 cabin grid
        self.area_location = None

    def get_player_name(self) -> str:
        return self.player_name

    def add_item(self, item: i.Item):
        self.item_inventory.append(item)

    def remove_item(self, item: i.Item) -> bool:
        if item in self.item_inventory:
            self.item_inventory.remove(item)
            return True
        else:
            return False

    def has_item(self, item: i.Item) -> bool:
        return item in self.item_inventory

    def print_inventory(self):
        for item in self.item_inventory:
            print(item.get_name())

    def move(self, direction: str, cabin) -> bool:
        x, y = self.room_location
        new_x, new_y = x, y  # Default to current position

        # Determine new position based on the direction
        if "left" in direction.lower() or "west" in direction.lower():
            if y > 0:
                new_y -= 1
            else:
                print("Its just a wall.")
        elif "right" in direction.lower() or "east" in direction.lower():
            if y < 2:
                new_y += 1
            else:
                print("Its just a wall.")
        elif "up" in direction.lower() or "north" in direction.lower():
            if x > 0:
                new_x -= 1
            else:
                print("Its just a wall.")
        elif "down" in direction.lower() or "south" in direction.lower():
            if x < 2:
                new_x += 1
            else:
                print("Its just a wall.")
        else:
            print("Please enter a valid command!")
            return False

        # Only update location if there's no wall
        if (new_x, new_y) != (x, y):
            self.room_location = (new_x, new_y)
            cabin.enter_area(new_x, new_y)
            return True

        return False
