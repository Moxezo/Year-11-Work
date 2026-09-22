class Room:
    def __init__(self,room_name,room_description,linked_rooms):
        self.name = room_name
        self.description = room_description
        self.linkedrooms = linked_rooms or {}
        self.characters = []
        self.item = []
        self.teams = []
    
    # Getters and Setters for Room Classed objects
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_character(self):
        return self.characters
    def get_item(self):
        return self.item
   
    def set_name(self,room_name):
        self.name = room_name
    def set_description(self, room_description):
        self.description = room_description
    def set_item(self, item):
        self.item = item
    def add_item(self,item):
        self.item.append(item)
    def set_character(self, characters):
        self.characters = characters
    def add_character(self,character):
        self.characters.append(character)
    
    # Prints the pbjects description to the terminal
    def describe(self):
        print(self.description)
    
    # Links a room to another room with a direction
    def link_room(self, room_to_link, direction):
        self.linkedrooms[direction] = room_to_link

    # Prints the linked rooms to the terminal
    def get_details(self):
        for direction in self.linkedrooms:
            room = self.linkedrooms[direction]
            print(f"The {room.get_name()} is {direction}")

    # Changes player location based on direction input
    def move(self,direction):
        if direction in self.linkedrooms:
            return self.linkedrooms[direction]
        else:
            print("You can't go that way!")
            return self