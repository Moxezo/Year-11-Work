from Characters import *
from Items import *
from Rooms import *
from Attacks import *

sword = Item("Iron Sword", "A sharp steel blade.")
enemy_claw = Item("Monster Claw", "Sharp natural weapons.")
annoying = Item("Annoying","You are annoying and can do things because of it.")


hero = Combatant("Player 1", "The main protagonist", 12, "Let's do this!")
ally = Combatant("Companion", "A trustworthy healer/fighter", 12, "I have your back!")

goblin_a = Combatant("Goblin Warrior", "A small green brute", 50, "Gah!")
goblin_b = Combatant("Goblin Archer", "A ranged nuisance", 40, "Hehehe!")


hero.pickup_item(sword)
ally.pickup_item(sword)
hero.pickup_item(annoying)
ally.pickup_item(annoying)
goblin_a.pickup_item(enemy_claw)
goblin_b.pickup_item(enemy_claw)


slash = Attack("Slash", range(20,31), "Swings the sword", "Slashes at", sword)
bite = Attack("Bite", 12, "Snaps jaws down", "bites", enemy_claw)
tickle = Attack("Tickle",0,"Does nothing","You tickle",annoying)

hero.learn_attack(slash)
ally.learn_attack(slash)
hero.learn_attack(tickle)
ally.learn_attack(tickle)
goblin_a.learn_attack(bite)
goblin_b.learn_attack(bite)


player_team = Team("Heroes")
player_team.add_member(hero)
player_team.add_member(ally)

enemy_team = Team("Goblins")
enemy_team.add_member(goblin_a)
enemy_team.add_member(goblin_b)


team_fight(player_team, enemy_team)