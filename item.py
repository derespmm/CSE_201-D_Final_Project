class Item:
    """A class to hold data for items."""
    def __init__(self, name, rarity, max_stack_size):
        self.name = name
        self.rarity = rarity
        self.max_stack_size = max_stack_size


class Inventory:
    """A class for a player inventory, showing a players items and amounts."""
    def __init__(self):
        self.item_list = [], []

    def add_item(self, item, amount=1):
        if item in self.item_list[0]:
            index = self.item_list[0].index(item)
            if self.item_list[1][index] + amount <= item.max_stack_size:
                self.item_list[1][index] += amount
                return True
            else:
                return False
        elif amount <= item.max_stack_size:
            self.item_list[0].append(item)
            self.item_list[1].append(amount)
            return True
        else:
            return False

    def remove_item(self, item, amount=1):
        index = self.item_list[0].index(item)
        if self.item_list[1][index] - amount == 0:
            self.item_list[0].remove(item)
            del self.item_list[-1][index]
            return True
        elif self.item_list[1][index] - amount >= 0:
            self.item_list[1][index] -= amount
            return True
        else:
            return False

    def has_item(self, item):
        if item in self.item_list[0]:
            return True
        else:
            return False
