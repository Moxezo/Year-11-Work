class Item():
    def __init__(self,item_name,item_description):
        self.name = item_name
        self.description = item_description
    
    # Getters and Setters for Items
    def set_name(self,item_name):
        self.name = item_name
    def set_description(self,item_description):
        self.description = item_description
   
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    
    # Prints objects description to terminal
    def describe(self):
        print(self.description)