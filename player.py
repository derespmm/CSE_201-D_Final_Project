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

    def move(self, direction: str) -> bool:
        if "left" in direction.lower():
            print("You moved left.")
        elif "right" in direction.lower():
            print("You moved right.")
        elif "up" in direction.lower():
            print("You moved up.")
        elif "down" in direction.lower():
            print("You moved down.")
        else:
            print("Please enter a valid command!")
            return False
        return True

    def print_inventory(self):
        for item in self.item_inventory:
            print(item.get_name())

    def run_command(self, command: str = "exit"):
        if "move" in command.lower():
            self.move(command)
        elif "inventory" in command.lower():
            self.print_inventory()
        elif "exit" in command.lower():
            return False
        elif "test" in command.lower():
            print("you tested a command")
        else:
            print("Please enter a valid command!")
        return True
