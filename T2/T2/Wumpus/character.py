class Character():
    def __init__(self,char_name,char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this char
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
    # Choose what this char says
    def set_conversation(self,conversation):
        self.conversation = conversation
    # Talk with this char
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesnt want to talk to you.")
    # Fight this char
    def fight(self,combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True
    def steal(self,stolen_item):
        print(f"You steal {self.name}'s {stolen_item}")
class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness = None
        Enemy.enemies_to_defeat += 1
    # Weakness management
    def get_weakness(self):
        return self.weakness
    def set_weakness(self,weakness):
        self.weakness = weakness
    # Fighting
    def fight(self,combat_item): 
        if combat_item.lower() == self.weakness:
            print(f"You successfully bash {self.name}'s skull in with your {combat_item}")
            Enemy.enemies_to_defeat -= 1
            return True
        else:
            print(f"{self.name} slimes yo ahh out")
            return False
            
class Friend(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.feeling = None
    def hug(self):
        if self.name == "Gauthak":
            print(f"Gauthak pushes you off him.")
            print(f'[{self.name} says]: Do not touch me.')
        else:
            print(f"You hug {self.name}. They hug you back!")
    def pat(self):
        if self.name == "Gauthak":
            print(f"Gauthak pushes you off him.")
            print(f'[{self.name} says]: Do not touch me.')
        else:    
            print(f"You pat {self.name}. They pat you back, good boy!")