from Items import *
import random

# Bar to separate sections of text
def section_border():
    print("================================================================================================================")

class Team():
    def __init__(self,team_name):
        self.name = team_name
        self.members = []

    # Adds a Combatant to the team members list
    def add_member(self,recruit):
        self.members.append(recruit)
        recruit.set_team(self)
    def join_team(self,recruit):
        self.members.append(recruit)
        recruit.set_team(self)
        print(f"{recruit.get_name()} joined your team!")


    # Returns a list of all alive members of the team
    def get_living_members(self):
        return [m for m in self.members if m.get_hp() > 0]
    
    # Returns True or False if all team members HP is 0
    def is_defeated(self):
        return len(self.get_living_members()) == 0
    
    # Getters and Setters for team class
    def get_name(self):
        return(self.name)
    def get_members(self):
        return self.members
    
    def set_name(self,name):
        self.name = name

class Character():
    def __init__(self,char_name,char_description,hp):
        self.name = char_name
        self.description = char_description
        self.hp = int(hp)
        self.inventory = []
        self.conversation = None
        self.team = None
        self.trades = {
            "give" : "",
            "reward" : ""
        }
        self.trade_msg = None
        
    # Setters and Getters for Characters
    def set_trade_msg(self,msg):
        self.trade_msg = msg
    def set_name(self,name):
        self.name = name
    def set_description(self,description):
        self.description = description
    def set_hp(self,hp):
        self.hp = hp
    def set_conversation(self,conversation):
        self.conversation = conversation
    def set_team(self,team):
        self.team = team
    def set_trades(self,trade_dict):
        self.trades = trade_dict

    def get_trade_msg(self):
        return self.trade_msg
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_hp(self):
        return self.hp
    def get_conversation(self):
        return self.conversation
    def get_inventory(self):
        return self.inventory
    def get_team(self):
        return self.team
    def get_trades(self):
        return self.trades
    
    # Adds an items to the trade dictionary
    def add_trade_give(self,value):
        self.trades["give"] = value
    def add_trade_reward(self,value):
        self.trades["reward"] = value

    # Allows user to give something in return for something else
    def trade(self,buyer):
        print(f"[{self.get_name()}] says: {self.trade_msg}")
        print("Do you wish to trade?")
        trade_yn = input("> ").lower()
        if trade_yn in ["y","yes","ye"]:
            if self.trades["give"] in buyer.inventory:
                buyer.inventory.remove(self.trades["give"])
                if isinstance(self.trades["reward"],Item):
                    buyer.pickup_item(self.trades["reward"])
                elif callable(self.trades["reward"]):
                    self.trades["reward"]()
                print(f"[{self.name}] says: Thank you for the trade.")
                self.set_trade_msg(None)
            else:
                print(f"[{self.name}] says: You don't have {self.trades["give"].get_name()}! Come back when you do.")
        else:
            print(f"[{self.name}] says: Your loss. Come back if you change your mind.")
            


    # Prints the objects conversation
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.get_name()}] says: {self.conversation}")
        else:
            print(f"{self.get_name()} doesn't want to talk to you.")

    # Appends the object to the Characters inventory list (for when playing)
    def pickup_item(self,item_add):
        if isinstance(item_add,Item):
            self.inventory.append(item_add)
            print(f"You add the {item_add.get_name()} to your inventory")
            inventory_names = [item.get_name() for item in self.inventory]
            print(f"Current inventory: {', '.join(inventory_names)}")
        else:
            print("You can't add that to your inventory!")
    
    # Appends object to Characters inventory list (for setup/hidden from player)
    def add_inventory(self,add_item):
        if isinstance(add_item,Item):
            self.inventory.append(add_item)
        else:
            pass
    
    # Method to fight someone. Won't let you fight unless they are Enemy class (Or super Enemy).
    def fight(self,opponent):
        print(f"You cannot fight {opponent.get_name()}")

class Combatant(Character):
    def __init__(self,char_name,char_description,hp,fight_msg):
        super().__init__(char_name,char_description,hp)
        self.fight_msg = fight_msg
        self.attacks = []
    
    # Getters and Setters for Enemy class
    def set_fight_msg(self,fight_msg):
        self.fight_msg = fight_msg
    def set_attacks(self,attack_list):
        self.attacks = attack_list

    def get_fight_msg(self):
        return self.fight_msg
    def get_attacks(self):
        return self.attacks

    # Adds an attack to the objects list of available attacks
    def learn_attack(self,attack_object):
        self.attacks.append(attack_object)
        print(f"{self.get_name()} learned {attack_object.get_name()}")
    def add_attack(self,attack_object):
        self.attacks.append(attack_object)
    
    """This is unfinished code that isn't used. Please ignore"""
    # def fight(self,opponent):   
    #     print("======================================================================================")
    #     print(f"BATTLE STARTED WITH {opponent.get_name()}")
    #     print(f"[{opponent.get_name()}] says: {opponent.get_fight_msg()}")

    #     while self.get_hp() > 0 and opponent.get_hp() > 0:
    #         print("=========================================================================================")
    #         print(f"Your HP: {self.get_hp()}\n Opponent HP: {opponent.get_hp()}")
    #         print("What will you do?")


# Runs a fight with the 2 teams inputted (Team1 is player controlled)
def team_fight(team1,team2):
    round_num = 1
    section_border()
    print(f"{team1.get_name()} VS {team2.get_name()}")
    section_border()
    while not team1.is_defeated() and not team2.is_defeated():
        section_border()
        print(f"Round: {round_num}")
        print(f"It is {team1.get_name()}'s turn")
        for attacker in team1.get_living_members():
            if team2.is_defeated():
                break
            section_border()
            print(f"---{attacker.get_name()}'s turn---")
            attacks = attacker.get_attacks()
            if not attacks:
                print(f"{attacker.get_name()} has no moves! You skip the turn")
                continue
            targets = team2.get_living_members()
            print("Who do you want to attack?")
            # Prints all useable targets with a corresponding number and lets user select one
            for idx, target in enumerate(targets, start=1):
                print(f"{idx}. {target.get_name()} ({target.get_hp()} HP)")
            try:
                target_choice = int(input("Pick a target # > ")) - 1
                if 0 <= target_choice < len(targets):
                    victim = targets[target_choice]
                else:
                    print("Invalid choice! You attack a random enemy.")
                    victim = random.choice(targets)
            except ValueError:
                print("Invalid choice! You attack a random enemy.")
                victim = random.choice(targets)
            section_border()
            print("Choose your attack:")
            # Prints all useable attacks with a corresponding number and lets user select one
            for idx, atk in enumerate(attacks, start=1):
                print(f"{idx}. {atk.get_name()} --> {atk.get_description()}")
            valid_atk_choice = False
            while valid_atk_choice == False:
                try:
                    atk_choice_number = int(input("Pick an attack # > ")) - 1
                    if 0 <= atk_choice_number < len(attacks):
                        atk_choice = attacks[atk_choice_number]
                        valid_atk_choice = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid Choice")
            section_border()
            atk_choice.use_atk(victim,attacker)
        # If the checks if there are still enemies alive
        if not team2.is_defeated():
            section_border()
            print(f"{team2.get_name()}'s turn")
            # Picks a random target and uses a random attack the enemy has on the target
            for attacker in team2.get_living_members():
                if team1.is_defeated():
                    break
                section_border()
                targets = team1.get_living_members()
                victim = random.choice(targets)
                attacks = attacker.get_attacks()
                if attacks:
                    atk_choice = random.choice(attacks)
                    atk_choice.use_atk(victim,attacker)
                else:
                    print(f"{attacker.get_name()} stands there menacingly.")
        round_num += 1
    if team1.is_defeated():
        print("You lost, you failed your mission")
    else:
        print(f"Congratulations! You defeated {team2.get_name()}")