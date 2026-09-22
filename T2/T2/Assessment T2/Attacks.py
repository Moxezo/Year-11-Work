from Characters import *
from Items import *
from Rooms import *
import random

class Attack():
    def __init__(self,name,dmg,description,use_msg,item_req):
        self.name = name
        self.description = description
        self.msg = use_msg
        self.item_req = item_req
        self.dmg = dmg

    # Getters and Setters for Attack
    def set_name(self,name):
        self.name = name
    def set_description(self,description):
        self.description = description
    def set_msg(self,use_msg):
        self.msg = use_msg
    def set_item_req(self,item_req):
        self.item_req = item_req
    def set_dmg(self,dmg):
        self.dmg = dmg

    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_msg(self):
        return self.msg
    def get_item_req(self):
        return self.item_req
    def get_dmg(self):
        return self.dmg

    # Uses the attack object and lowers the victims health
    def use_atk(self,victim,user):
        user_inventory_names = [item.get_name() for item in user.get_inventory()]
        if self.item_req.get_name() in user_inventory_names:
            print(f"{user.get_name()} {self.msg} {victim.get_name()}")
            if isinstance(self.get_dmg(),range):
                actual_dmg = random.choice(self.get_dmg())
            else:
                actual_dmg = self.get_dmg()
            victim.hp -= actual_dmg
            print(f"It deals {actual_dmg} damage!")
            print(f"[{victim.get_name()}'s HP]: {max(0, victim.hp)}")
        else:
            print(f"{user.get_name()} doesn't have the item they need!")