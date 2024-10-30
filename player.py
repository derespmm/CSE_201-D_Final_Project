import item as i

class Player:
    def __init__(self, name: str, current_room=None):
        self.player_name = name
        self.item_inventory = []
        self.notes_inventory = []
        self.room_location = (1, 1)  # Player starts at the center tile
        self.current_room = current_room  # Reference to the current room

    # Method to set the current room (useful for switching areas)
    def set_current_room(self, room):
        self.current_room = room

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

    def has_item(self, item_name: str) -> bool:
        return any(item.get_name() == item_name for item in self.item_inventory)

    def print_inventory(self):
        if not self.item_inventory:
            print("Your inventory is empty.")
        else:
            print("You have the following items in your inventory:")
            for item in self.item_inventory:
                print(f"- {item.get_name()}: {item.get_description()}")

    def inspect_item(self, item_name: str):
        """Inspect an item in the inventory and display its description."""
        for item in self.item_inventory:
            if item.get_name().lower() == item_name.lower():
                print(item.get_inspection_text())
                return
        print(f"You don't have an item named '{item_name}' in your inventory.")

    def move(self, direction: str) -> bool:
        x, y = self.room_location
        new_x, new_y = x, y  # Default to current position

    # Determine new position based on the direction
        if "left" in direction.lower() or "west" in direction.lower():
            if y > 0:
                new_y -= 1
            else:
                print("It's just a wall.")
                return False 
        elif "right" in direction.lower() or "east" in direction.lower():
            if y < 2:
                new_y += 1
            else:
                print("It's just a wall.")
                return False
        elif "up" in direction.lower() or "north" in direction.lower():
            if x > 0:
                new_x -= 1
            else:
                print("It's just a wall.")
                return False
        elif "down" in direction.lower() or "south" in direction.lower():
            if x < 2:
                new_x += 1
            else:
                print("It's just a wall.")
                return False
        else:
            print("Please enter a valid command!")
            return False

    # Only update location if there's no wall
        if (new_x, new_y) != (x, y):
            self.room_location = (new_x, new_y)
            self.current_room.enter_area(new_x, new_y)  # Call enter_area to print the description
            return True

        return False

        # Only update location if there's no wall
        if (new_x, new_y) != (x, y):
            self.room_location = (new_x, new_y)
            cabin.enter_area(new_x, new_y)
            return True

        return False
