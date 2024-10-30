import item as i


class Player:
    """A class for the player character."""

    def __init__(self, name: str):
        self.player_name = name
        self.item_inventory = []
        self.notes_inventory = []
        self.room_location = None
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
        if item in self.item_inventory:
            return True
        else:
            return False

    def print_inventory(self):
        for item in self.item_inventory:
            print(item.get_name())

    def move(self, direction: str) -> bool:
        if "left" in direction.lower() or "west" in direction.lower():
            print("You moved left.")
        elif "right" in direction.lower() or "east" in direction.lower():
            print("You moved right.")
        elif "up" in direction.lower() or "north" in direction.lower():
            print("You moved up.")
        elif "down" in direction.lower() or "south" in direction.lower():
            print("You moved down.")
        else:
            print("Please enter a valid command!")
            return False
        return True
