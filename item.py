class Item:
    """A class to hold data for items."""
    def __init__(self, name: str, description: str, inspection_text: str = None):
        self.name = name
        self.description = description
        self.inspection_text = inspection_text or description  # Default to description if none provided
        
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description
    
    def get_inspection_text(self) -> str:
        return self.inspection_text
    
    def use_item(self):
        print("You used the", self.name + "!")
