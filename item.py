class Item:
    """A class to hold data for items."""
    def __init__(self, name: str, desciption: str):
        self.name = name
        self.desciption = desciption
        
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.desciption
    
    def use_item(self):
        print("You used the", self.name + "!")
