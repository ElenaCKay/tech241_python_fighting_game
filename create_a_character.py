import random

race = ["Human", "Elf", "Hobbit", "Dwarf"]

class_skill = {
    "Guardian": {"health": 35, "attack": 4, "heal": 0, "items": []},
    "Hunter": {"health": 25, "attack": 5, "heal": 1, "items": []},
    "Rogue": {"health": 25, "attack": 6, "heal": 0, "items": []},
    "Druid": {"health": 23, "attack": 4, "heal": 3, "items": []},
    "Bard": {"health": 23, "attack": 3, "heal": 6, "items": []}
}

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

warrior = {
    "name": "",
    "race": "",
    "class": "",
    "class_stats": {},
    "title": ""
}


def create_character(name):

    warrior["name"] = name

    # Creates a random title
    title = random.choice(list(fantasy_titles))
    warrior["title"] = title

    # Pick a race
    print(f"Hello {name} {title}! Pick a race from the following {race}")
    player_race = input().capitalize()

    picked_race = False

    while not picked_race:
        if player_race not in race:
            print("I do not recognise that race... Pick again")
        else:
            picked_race = True
            warrior["race"] = player_race
    print(f"You have chosen {player_race}\n")

    # Pick a class
    class_list = list(class_skill.keys())

    print(f"Pick a class from the following {class_list} ")
    player_class = input().capitalize()

    picked_class = False

    while not picked_class:
        if player_class not in class_skill.keys():
            print("I do not recognise that class... Pick again")
        else:
            picked_class = True
            warrior["class"] = player_class
            warrior["class_stats"] = class_skill[player_class]
    print(f"You have chosen {player_class}\n")

    return warrior
