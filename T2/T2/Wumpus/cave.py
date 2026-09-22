import re


class Cave:
    def __init__(self,cave_name,cave_description,linked_caves):
        self.name = cave_name
        self.description = cave_description
        self.linkedcaves = linked_caves or {}
        self.character = None
        self.item = None
    
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def set_name(self,cave_name):
        self.name = cave_name
    def set_description(self, cave_description):
        self.description = cave_description
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item
    
    def describe(self):
        print(self.description)
    
    def link_cave(self, cave_to_link, direction):
        self.linkedcaves[direction] = cave_to_link

    def get_details(self):
        for direction in self.linkedcaves:
            cave = self.linkedcaves[direction]
            print(f"The {cave.get_name()} is {direction}")

    def move(self,direction):
        if direction in self.linkedcaves:
            return self.linkedcaves[direction]
        else:
            print("You can't go that way!")
            return self
