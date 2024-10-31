import item as i
import room as r

class Player:
    def __init__(self, name: str, current_room: r.Room):
        self.player_name = name
        self.item_inventory = []
        self.notes_inventory = []
        self.room_location = (1, 1)  # Player starts at the center tile
        self.current_room = current_room  # Reference to the current room

    # Method to set the current room (useful for switching areas)
    def set_current_room(self, room):
        self.current_room = room
    
    # Returns players name
    def get_player_name(self) -> str:
        return self.player_name
    
    # Adds an item to the players inventory
    def add_item(self, item: i.Item):
        self.item_inventory.append(item)

    # Removes item from players inventory then returns true, If item is not present returns false.
    def remove_item(self, item: i.Item) -> bool:
        if item in self.item_inventory:
            self.item_inventory.remove(item)
            return True
        else:
            return False

    # Returns true if item is in players inventory, false o.w.
    def has_item(self, item_name: str) -> bool:
        return any(item.get_name() == item_name for item in self.item_inventory)

    # Prints items in the inventory, if empty "Your inventory is empty" will be printed.
    def print_inventory(self):
        if not self.item_inventory:
            print("Your inventory is empty.")
        else:
            print("You have the following items in your inventory:")
            for item in self.item_inventory:
                print(f"- {item.get_name()}: {item.get_description()}")
    
    # Inspect an item in the inventory and display its description.
    def inspect_item(self, item_name: str):
        for item in self.item_inventory:
            if item.get_name().lower() == item_name.lower():
                print(item.get_inspection_text())
                return
        print(f"You don't have an item named '{item_name}' in your inventory.")

    # Moves the player
    def move(self, direction: str) -> bool:
        x, y = self.room_location
        new_x, new_y = x, y  # Default to current position

    # Determine new position based on the direction
        if "left" in direction.lower() or "west" in direction.lower():
            if x > 0:
                new_x -= 1
            else:
                print("It's just a wall.")
                return False 
        elif "right" in direction.lower() or "east" in direction.lower():
            if x < self.current_room.size - 1:
                new_x += 1
            else:
                print("It's just a wall.")
                return False
        elif "up" in direction.lower() or "north" in direction.lower():
            if y > 0:
                new_y -= 1
            else:
                print("It's just a wall.")
                return False
        elif "down" in direction.lower() or "south" in direction.lower():
            if y < self.current_room.size - 1:
                new_y += 1
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
