from Characters import *
from Items import *
from Rooms import *
from Attacks import *

# Setup for a list with dicts of all available commands
move_cmd = {
    "name" : "Move",
    "msg" : 'Lets you move in a direction. Performed by inputting one of the following: "north", "east", "south", "west".'
}
fight_cmd = {
    "name" : "Fight",
    "msg" : 'Initiates combat with all Combatants in the current room. Performed by inputting "fight".'
}
trade_cmd = {
    "name" : "Trade",
    "msg" : 'Allows you to trade with certain characters. Will remove the item you give from your inventory. Performed by inputting "trade"'
}
talk_cmd = {
    "name" : "Talk",
    "msg" : 'Lets you pick a character to speak to, and they will say a unique message. Some characters will provide useful info. Performed by typing "talk"'
}
describe_cmd = {
    "name" : "Describe",
    "msg" : 'Describes a character or item of your choice that is in the current room. Performed by inputting "describe"'
}
take_cmd = {
    "name" : "Take",
    "msg" : 'Lets you take pickup an item of your choice in the current room. Performed by inputing "take"'
}
cmd_list = [
    move_cmd, fight_cmd, trade_cmd, talk_cmd, describe_cmd, take_cmd
]

current_room_chars = []

# chamber setup
chamber = Room("Throne Room","A vast room, marble pillars, ornate engravings, and in the centre lays a golden throne with silk upholstery, sat atop is the King you strive to defeat. He has a glass of wine in his hand, and he doesn't notice as you peer into the room.","")
library = Room("Library","A large, well kept library. A variety of different books line the shelves. In the centre there is a help desk.","")
garden = Room("Royal Garden","A large area full of well-kept greenery, and a variety of exotic plants in many vibrant colours.","")
dining = Room("Dining Hall","A long, candlelit room with a large table to match. The table has a red tablecloth draped all the way across it, with empty plants distributed across.","")
barracks = Room("Barracks","A cramped room full of bunks. There are many soldiers throughout the area, each performing tasks such as polishing their armour, or sharpening their spear.","")

# Room layout
chamber.link_room(library,"west")
library.link_room(chamber,"east")
chamber.link_room(garden,"south")
garden.link_room(chamber,"north")
barracks.link_room(garden,"west")
garden.link_room(barracks,"east")
dining.link_room(chamber,"west")
chamber.link_room(dining,"east")

# Item setup
joke_book = Item("Joke Book","A purple book full of strange jokes and insults.")
library.add_item(joke_book)
shiny_stone = Item("Shiny Stone","A glistening rock. Upon closer inspection, you realise it's a premium sharpening stone.")
garden.add_item(shiny_stone)

# Player setup
sword = Item("Longsword","A steel longsword used by most Knights.")
slash = Attack("Slash",range(15,26),"A basic sword slash (Deals 15-25 damage)","swings their sword sideways in a slash at",sword)
player = Combatant("The Knight","You. A Knight in dark black armour.",100,"")
player.add_inventory(sword)
player.add_attack(slash)

# Jester setup
jester_quips = ["You look like a million bucks, all of it in small, useless copper coins.","I would insult your intelligence, but I don't want to explain what an insult is.","Let's make a quick deal. You roll on the ground and bark like a dog, and I'll give you a free swing at me. See? It doesn't cost a thing!","In the kingdom of laughter, the jester wears the real crown.","Behind every great king is a jester whispering the actual good ideas."]
jester_cane = Item("Jester's Cane","A bedazzled cane to be used by the royal Jester")
jester_luckatk = Attack("Jester's Gamble",range(1,51),"The Jester uses his cane to shoot a beam of energy (Deals 1-50 damage)","flicks his cane and a glowing, pastel pink bolt of light shoots out and collides with",jester_cane)
jester_flatatk = Attack("Jester's Quip",30,"The Jester says a quip to harm the enemies will (Deals 30 damage)",f"says: {random.choice(jester_quips)} -->",jester_cane)
jester = Combatant("The Jester","A bouncy jester in a red and blue jester's outfit.",100,"This will be fun!")
jester.set_conversation("I know I seem jovial, but I hate the King just as much as you")
jester.add_attack(jester_flatatk)
jester.add_attack(jester_luckatk)
jester.add_inventory(jester_cane)
dining.add_character(jester)
jester.set_trade_msg("If you give me something for my jests, I'll join your team! (Give Joke Book)")

# Soldiers setup
soldier_weapons = Item("Soldier's Arms","The Spears, bows, and Swords used by soldiers of the Royal Army")
soldier_groupatk = Attack("Basic Formation",35,"The soldiers take a textbook battle formation and strike at the enemy (Deals 35 damage)","The soldiers take an arrow formation and attack",soldier_weapons)
soldier_archer = Attack("Archer Shot", range(20,46),"The archer shoots their bow at the enemy (Deals 20-45 damage)","The soldier with a bows kneels down and shoots an arrow at",soldier_weapons)
soldiers = Combatant("The Soldiers","A small group of soldiers from the Royal Army.",120,"We trained for this!")
soldiers.add_attack(soldier_groupatk)
soldiers.add_attack(soldier_archer)
barracks.add_character(soldiers)
soldiers.set_trade_msg("The King treats us like dirt! We'll join you if you help us prepare. (Give Shiny Stone)")
soldiers.set_conversation("The King keeps sending us on death missions! We lost half our numbers a week ago.")
soldiers.add_inventory(soldier_weapons)

# Librarian setup
librarian = Character("Vesper","A woman with long, dark purple hair, strands fall down over her eyes. She leans on her desk and her large hair is spread over its surface.",999999999999999999)
library.add_character(librarian)
librarian.set_conversation("Welcome, Knight. I assume you aren't here for light reading, so I'll cut to the chase and tell you the info you seek.\n - The Soldiers in the barracks have a soft spot for a good sharpening stone. \n - The Jester will side with anyone who can help him with comedy.")
"""This was for debugging the trade system"""
# librarian.set_trade_msg("test")
# librarian.add_trade_give(sword)
# librarian.add_trade_reward(func_test)

# King setup
kings_sword = Item("Kings Greatsword", "A long greatsword with ornate engravings and golden inlays. The pommel has a ruby embedded in the end")
king_atk1 = Attack("Royal blade",range(50,91),"Thilvar swings his greatsword in a heavy downward strike (Deals 50-90 dmg)","lifts his Royal Greatsword high above his head and slams it down into", kings_sword)
king = Combatant("King Thilvar", "A middle aged man in a regal, crimson robe. He has a sharp beard with small streaks of grey, and a bald head, with a golden crown sat atop.", 200, "Very well, I shall squash you like the peasant you are!")
king.add_attack(king_atk1)
king.add_inventory(kings_sword)
chamber.add_character(king)

# Team setup
heroes = Team("Anti-Royals")
heroes.add_member(player)
jester.set_trades({"give" : joke_book, "reward" : lambda: heroes.join_team(jester)})
soldiers.set_trades({"give" : shiny_stone,"reward" : lambda: heroes.join_team(soldiers)})

# Testing code
# player.add_inventory(joke_book)

first_cycle = True
current_room = garden
# Command function defining
def take_func():
    if len(current_room.get_item()) > 0:
        print("Items in the room:")
        for idx, item in enumerate(current_room.get_item(),start=1):
            print(f"{idx}. {item.get_name()} --> {item.get_description()}")
        print("What Item do you want to take?")
        valid_item_take = False
        while valid_item_take == False:
            try:
                take_choice_number = int(input("Pick an Item # > ")) - 1
                if 0 <= take_choice_number < len(current_room.get_item()):
                    take_choice = current_room.get_item()[take_choice_number]
                    valid_item_take = True
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        player.pickup_item(take_choice)
        current_room.item.remove(take_choice)
    else:
        print("There's nothing in here to take!")
def describe_func():
    section_border()
    if len(current_room.get_item()) > 0 and len(current_room.get_character()) > 0:
        print("Do you want to describe an Item or a Character?")
        object_describe_choice = input("> ").lower().strip()
        if object_describe_choice in ["i","item"]:
            print("Items in the room:")
            for idx, item in enumerate(current_room.get_item(),start=1):
                print(f"{idx}. {item.get_name()}")
            print("What Item do you want to describe?")
            valid_item_describe = False
            while valid_item_describe == False:
                try:
                    describe_choice_number = int(input("Pick an Item # > ")) - 1
                    if 0 <= describe_choice_number < len(current_room.get_item()):
                        describe_choice = current_room.get_item()[describe_choice_number]
                        valid_item_describe = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            print(describe_choice.get_description())
        else:
            print("Characters in the room:")
            for idx, char in enumerate(current_room.get_character(),start=1):
                print(f"{idx}. {char.get_name()}")
            print("What Character do you want to describe?")
            valid_char_describe = False
            while valid_char_describe == False:
                try:
                    describe_choice_number = int(input("Pick a character # > ")) - 1
                    if 0 <= describe_choice_number < len(current_room.get_character()):
                        describe_choice = current_room.get_character()[describe_choice_number]
                        valid_char_describe = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            print(describe_choice.get_description())
    elif len(current_room.get_item()) > 0:
            print("Items in the room:")
            for idx, item in enumerate(current_room.get_item(),start=1):
                print(f"{idx}. {item.get_name()}")
            print("What Item do you want to describe?")
            valid_item_describe = False
            while valid_item_describe == False:
                try:
                    describe_choice_number = int(input("Pick an Item # > ")) - 1
                    if 0 <= describe_choice_number < len(current_room.get_item()):
                        describe_choice = current_room.get_item()[describe_choice_number]
                        valid_item_describe = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            print(describe_choice.get_description())
    elif len(current_room.get_character()) > 0:
        print("Characters in the room:")
        for idx, char in enumerate(current_room.get_character(),start=1):
            print(f"{idx}. {char.get_name()}")
        print("What Character do you want to describe?")
        valid_char_describe = False
        while valid_char_describe == False:
            try:
                describe_choice_number = int(input("Pick a character # > ")) - 1
                if 0 <= describe_choice_number < len(current_room.get_character()):
                    describe_choice = current_room.get_character()[describe_choice_number]
                    valid_char_describe = True
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        print(describe_choice.get_description())
    else:
        print("There's nothing in here to describe")
def talk_func():
    if len(current_room.get_character()) > 0:
        section_border()
        print("People you can talk to:")
        for idx, char in enumerate(current_room.get_character(), start=1):
            print(f"{idx}. {char.get_name()}")
        print("Who do you want to talk to?")
        valid_talk_choice = False
        while valid_talk_choice == False:
            try:
                talk_choice_num = int(input("Choose a character # > ")) - 1
                if 0 <= talk_choice_num < len(current_room.get_character()):
                    talk_choice = current_room.get_character()[talk_choice_num]
                    valid_talk_choice = True
            except ValueError: 
                print("Invalid choice!")
        talk_choice.talk()
    else:
        print("There's no one here to talk to!")
def help_func():
    cmd_help_needed = True
    while cmd_help_needed == True:
        section_border()
        print("All available commands:")
        for idx, cmd in enumerate(cmd_list, start=1):
                print(f"{idx}. {cmd["name"]}")
        valid_help_choice = False
        while valid_help_choice == False:
                print('What command do you want to ask about? (Input the number of the command, or type "done" to exit)')
                cmd_help_num = input("> ")
                try:
                    cmd_help_num = int(cmd_help_num) - 1
                    if 0 <= cmd_help_num < len(cmd_list):
                        help_choice = cmd_list[cmd_help_num]
                        print(f"{help_choice['name']} --> {help_choice['msg']}")
                        valid_help_choice = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    if cmd_help_num == "done":
                        cmd_help_needed = False
                        valid_help_choice = True
                    else:
                        print("Invalid choice!")
def fight_func():
    room_chars = current_room.get_character()
    room_enemies = []
    for char in room_chars:
        if isinstance(char,Combatant) and char not in heroes.get_members():
            room_enemies.append(char)
    if len(room_enemies) > 0:
        enemy_team = Team("Opponent")
        for enemy in room_enemies:
            enemy_team.add_member(enemy)
        if len(enemy_team.get_members()) == 1:
            enemy_team.set_name(enemy_team.get_members()[0].get_name())
        team_fight(heroes,enemy_team)
    else:
        print("There's no one in here you can fight!")
def trade_func():
    if len(current_room.get_character()) > 0:
        tradeable_chars = []
        for char in current_room.get_character():
            if char.get_trade_msg() is not None:
                tradeable_chars.append(char)
        if len(tradeable_chars) > 0:
            print("All available traders:")
            for idx, char in enumerate(tradeable_chars, start=1):
                print(f"{idx}. {char.get_name()}")
            valid_trade_choice = False
            while valid_trade_choice == False:
                try:
                    trade_choice_number = int(input("Pick a trader # > ")) - 1
                    if 0 <= trade_choice_number < len(tradeable_chars):
                        trade_choice = tradeable_chars[trade_choice_number]
                        valid_trade_choice = True
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            trade_choice.trade(player)
        else:
            print("There's no one here you can trade with!")
    else:
        print("There's no one in here to trade with!")

while len(heroes.get_living_members()) > 0 and king.get_hp() > 0:
    while first_cycle == True:
        section_border()
        print("You were a high ranking member of King Thilvar's royal guard in the Faedrun Empire.\n" \
        "A year ago Thilvar betrayed you by leaving you to die on the battlefield.\n" \
        "Miraculously you survived, and now it is your mission to slay the King, and end the Faedrun Empire's reign.")
        print('--- You can input "help" for a list of commands ---')
        first_cycle = False
    for char in heroes.get_living_members():
        if char not in current_room.get_character():
            current_room.characters.append(char)
    current_room.characters.remove(player)
    for living_check in current_room.get_character():
        if living_check.get_hp() <= 0:
            current_room.characters.remove(living_check)
    section_border()
    print(f"You're in the {current_room.get_name()}")  
    print(current_room.get_description())
    print("---")
    current_room.get_details()
    print("---")
    if len(current_room.get_character()) >0:
        current_room_chars = [char.get_name() for char in current_room.get_character()]
        print(f"People in the room: {', '.join(current_room_chars)}")
    else:
        print(f"The {current_room.get_name()} has no people of note inside.")
    print("---")
    if len(current_room.get_item()) > 0:
        current_room_items = [item.get_name() for item in current_room.get_item()]
        print(f"Items in the room: {', '.join(current_room_items)}")
    else:
        print("There are no notable Items in here.")
    command = input("> ").lower().strip()
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "help":
        help_func()
    elif command == "fight":
        fight_func()
    elif command == "trade":
        trade_func()
    elif command == "talk":
        talk_func()
    elif command == "describe":
        describe_func()
    elif command == "take":
        take_func()
    elif command == "up up down down left right left right b a start":
        king.set_hp(0)
    else:
        print("That is not a valid choice!")
section_border()
if king.get_hp() <= 0:
    if player.get_hp() > 0:
        print("Great job young Knight. \nYou succesfully ended the corruption plagueing your life. \nCongratulations on living to tell the tale.")
    else:
        print("Despite losing your life, your allies kept fighting for you and managed to end the King's cirruption. \nHe will never betray anyone again.")
else:
    print("A valiant attempt, young Knight.\nIf you desire, you may be reborn, and attempt once more to end the King's reign.")