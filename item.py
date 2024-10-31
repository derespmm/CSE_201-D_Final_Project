# A class to hold data for items. 
class Item:
    
    # Initialize name, description, and insepction text for item. 
    def __init__(self, name: str, description: str, inspection_text: str = None):
        self.name = name
        self.description = description
        self.inspection_text = inspection_text or description  # Default to description if none provided
        
    # Gets the name and returns name of item. 
    def get_name(self) -> str:
        return self.name
    
    # Gets the description and returns description of item. 
    def get_description(self) -> str:
        return self.description
    
    # Returns inspection text of the item. 
    def get_inspection_text(self) -> str:
        return self.inspection_text
    
    # Returns the name of item used 
    def use_item(self):
        print("You used the", self.name + "!")
