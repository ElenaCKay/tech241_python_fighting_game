# Make a game where two character fight each other
# Choose your difficulty level (This will choose the enemy Goblin, Orc, Troll, Balrog)
# Choose your race (Human, Elf, Hobbit, Dwarf)
# Choose your class (Guardian, Hunter, Rogue, Druid, Bard)
# If defeated maybe they can drop health potions?
import sys
import random
from utils import pick_random_item

fantasy_titles = [
    "The Great",
    "The Ferocious",
    "The Enchanted",
    "The Mighty",
    "The Legendary",
    "The Cursed",
    "The Lost",
    "The Sacred",
    "The Brave",
    "The Shadowed",
    "The Wise",
    "The Fearless",
    "The Valiant",
    "The Magical",
    "The Ancient",
    "The Radiant",
    "The Bold",
    "The Fabled",
    "The Noble",
    "The Immortal"
]

enemies = {
    "Easy": {"creature": "Goblin", "health": 15, "attack": 2},
    "Medium":  {"creature": "Orc", "health": 20, "attack": 4},
    "Hard":  {"creature": "Troll", "health": 25, "attack": 4},
    "Impossible":  {"creature": "Balrog", "health": 30, "attack": 5}
}
enemy = "Goblin"

race = ["Human", "Elf", "Hobbit", "Dwarf"]

items = {
    "Dagger": {"attack": 2, "armour": 0},
    "Axe":  {"attack": 3, "armour": 0},
    "Sword": {"attack": 4, "armour": 0},
    "Shield": {"attack": 0, "armour": 3},
    "Cloak": {"attack": 0, "armour": 1},
    "Bow": {"attack": 3, "armour": 0},
    "Health elixir": {"attack": 0, "armour": 6},
    "Empower elixir": {"attack": 3, "armour": 0},
}

class_skill = {
    "Guardian":  {"health": 35, "attack": 4, "heal": 0, "items": []},
    "Hunter":  {"health": 25, "attack": 5, "heal": 1, "items": []},
    "Rogue":  {"health": 25, "attack": 6, "heal":  0, "items": []},
    "Druid":  {"health": 23, "attack": 4, "heal": 3, "items": []},
    "Bard":  {"health": 23, "attack": 3, "heal": 6, "items": []}
}

name = input("Welcome warrior, what is your name?  ").capitalize()

title = random.choice(list(fantasy_titles))

print(f"Hello {name} {title}! Pick a race from the following {race}")
player_race = input().capitalize()

picked_race = False

while not picked_race:
    if player_race not in race:
        print("I do not recognise that race... Pick again")
    else:
        picked_race = True
print(f"You have chosen {player_race}")

class_list = list(class_skill.keys())

print(f"Pick a class from the following {class_list}")
player_class = input().capitalize()

picked_class = False

while not picked_class:
    if player_class not in class_skill.keys():
        print("I do not recognise that race... Pick again")
    else:
        picked_class = True
print(f"You have chosen {player_class}")

difficulty = input("Choose a difficulty level: Easy, Medium, Hard, Impossible ").capitalize()

picked_difficulty = False

while not picked_difficulty:
        if difficulty not in enemies.keys():
            print("Pick a difficulty again... ")
        else:
            enemy = enemies[difficulty]["creature"]
            picked_difficulty = True

print(f"You have chosen {difficulty}.")

print(f"Watch out! A {enemy} approaches!")

enemy_attack = enemies[difficulty]["attack"]
enemy_health = enemies[difficulty]["health"]
players_attack = class_skill[player_class]["attack"]
players_heal = class_skill[player_class]["heal"]
players_health = class_skill[player_class]["health"]

while enemy_health > 0 and players_health > 0:
    attack_or_heal = input(f"You can attack or heal  ").capitalize()
    if attack_or_heal == "Attack":
        enemy_health -= players_attack
        print(f"Ouch! {enemy} has {enemy_health} health left!")
    if attack_or_heal == "Heal":
        players_health += players_heal
        print(f"You healed! +{players_heal} health")
    players_health -= enemy_attack
    print(f"{enemy} attacks! You have {players_health} health remaining!")

if enemy_health <= 0:
    print(f"Congratulations! {enemy} had been defeated!")
    random_item_name, random_item_stats = pick_random_item(items)
    print(f"{enemy} dropped a {random_item_name}!")
    class_skill[player_class]["items"].append(random_item_name)

   # Need to put everything in a loop for this to work.
    difficulty = input("Choose a new difficulty? Easy, Medium, Hard, Impossible ")
    picked_difficulty = False

if players_health <= 0:
    sys.exit("You Died!")


