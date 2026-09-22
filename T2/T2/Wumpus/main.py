from cave import Cave
from character import *
from item import *
import random

def fightfunc():
    global dead
    while True:
        print("What will you fight with?")
        print(f"Items in bag: {", ".join(bag)}")
        fight_with = input("> ")
        if fight_with.lower() in bag:
            break
        else:
            print(f"You don't have a {fight_with} in your bag! Try again.")
    if inhabitant.fight(fight_with) == True:
        if inhabitant is tungtung:
            current_cave.set_item(missile)
            current_cave.set_character(None)
        else:
            print("Good job you killed it you monster.")
            current_cave.set_character(None)
            if Enemy.enemies_to_defeat == 0:
                print("Congratulations hero, you live to tell the tale.")
                dead = True
    else:
        print("Game over :(")
        dead = True

cavern = Cave("Cavern","Damp, jagged cave, with stalactites hanging low from the tall ceiling","")
grotto = Cave("Grotto","A lush cave, with large clumps of moss, with a small stream flowing through the center of the cave","")
dungeon = Cave("Dungeon","A cubic room with stone brick walls. The faint, metallic smell of dried blood enters your nose, and you see various chains and tools around the walls","")
boss_room = Cave("Boss Room","A large cubic room, torches held on pillars illuminate the room. In the centre, a wumpus stands, expression blank. Staring. At you.","")

cavern.link_cave(dungeon,"north")
dungeon.link_cave(cavern,"south")
dungeon.link_cave(grotto,"west")
grotto.link_cave(dungeon,"east")

harry = Enemy("Harry","A smelly Wumpus")
harry.set_conversation("You're a fat little chud")
harry.set_weakness("magic missile")
dungeon.set_character(harry)

gauthak = Friend("Gauthak","A hulking Goliath with plate armour and a greatsword. He stands tall, looking down at you, judging your strength.")
gauthak.set_conversation("Hello little one. Do you have peanut butter? If so, I'll give you a weapon in exchange.")
grotto.set_character(gauthak)

pb = Item("Peanut Butter","a jar of peanut butter that never runs out no matter what.")
cavern.set_item(pb)

missile = Item("Magic Missile", "A scroll that allows you to cast a spell. It shoots 3 purple bolts of magic wherever the caster wishes.")

tungtung = Enemy("Tung Tung Tung Tung Tung Tung Tung Tung Tung Sahur","A walking baseball bat man, with a baseball bat in his right hand")
tungtung.set_conversation("TUNG TUNG TUNG TUNG TUNG TUNG TUNG TUNG TUNG TUNG SAHUR!")
tungtung.set_weakness("fish bat")
cavern.set_character(tungtung)

current_cave = cavern
dead = False
bag = []
bag.append("sword")


while dead == False:
    print("\n")
    print("=======================================================================")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_cave.get_item()
    if item is not None:
        print(f"In the {current_cave.get_name()} you notice {item.get_description()}")
    command = input(">").lower()
    if command in ["north","south","east","west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None and inhabitant is not gauthak:
            inhabitant.talk()
        elif inhabitant is not None and inhabitant is gauthak:
            inhabitant.talk()
            print("Do you want to trade with Gauthak (Yes/No)")
            trade_gauthak = input(">")
            if "peanut butter" in bag:
                if trade_gauthak.lower() in ["yes","y","ye"]:
                    bag.remove("peanut butter")
                    print(f"[{inhabitant.name} says]: Thank you, here is your weapon")
                    print("He hands you a large baseball bat, however it is made of a large fish. It's rock hard.")
                    bag.append("fish bat")
                else:
                    print("Your loss weakling.")
            else:
                print("You do not have peanut butter.")
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant,Enemy):
            fightfunc()
        elif inhabitant is not None and  not isinstance(inhabitant, Enemy):
            print("Don't fight them!")
        else:
            print("Blud there's no one here :|")
    elif command == "steal":
        if inhabitant is not None:
            print("What do you want to steal?")
            stealchoice = input(">")
            if isinstance(inhabitant,Friend):
                inhabitant.steal(stealchoice)
                bag.append(stealchoice)
                print("You're mean, they are your friend!")
            elif isinstance(inhabitant,Enemy):
                inhabitant.steal(stealchoice)
                bag.append(stealchoice)
                stealfight = random.choice([1,2])
                if stealfight == 1:
                    fightfunc()    
                else:
                    print(f"{inhabitant.name} didn't notice you stealing from them. Good job!")
        else:
            print("There's no one to steal from.")
    elif command == "pat":
        if inhabitant is not None and isinstance(inhabitant,Friend):
            inhabitant.pat()
        elif inhabitant is not None and isinstance(inhabitant,Enemy):
            print("Not a great idea. You might get stabbed!")
        else:
            print("There's no one here")
    elif command == "hug":
        if inhabitant is not None and isinstance(inhabitant,Friend):
            inhabitant.hug()
        elif inhabitant is not None and isinstance(inhabitant,Enemy):
            print("Not a great idea. You might get stabbed!")
        else:
            print("There's no one here")
    elif command == "take":
        if item is not None:
            print(f"You put the {item.get_name()} in your backpack")
            bag.append(item.get_name().lower())    
            current_cave.set_item(None)
        else:
            print(f"There's nothing in the {current_cave} to take.")
    # elif command == "trade":
    #     if current_cave.get_character() == gauthak:
    #         if pb in bag:
    #             print()
    else:
        print("That's not a command.")