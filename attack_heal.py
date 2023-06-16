from random import randint

enemies = {
    "Easy": {"creature": "Goblin", "health": 15, "attack": 2},
    "Medium":  {"creature": "Orc", "health": 20, "attack": 4},
    "Hard":  {"creature": "Troll", "health": 25, "attack": 4},
    "Impossible":  {"creature": "Balrog", "health": 30, "attack": 5}
}


def warrior_attack(warrior, difficulty):

    #warrior_attack = True

    warrior_attack = warrior["class_stats"]["attack"]
    warrior_health = warrior["class_stats"]["health"]
    enemy_attack = enemies[difficulty]["attack"]
    enemy_health = enemies[difficulty]["health"]
    warrior_initiative = randint(1, 20)
    enemy_initiative = randint(1, 20)

    if warrior_initiative == 1:
        warrior_health -= 1
        print("You trip on a rock and somehow punch yourself in the face...\n")
        print(f"{warrior['name']} health left: {warrior_health}")

    elif enemy_initiative == 1:
        double_attack = warrior_attack * 2
        enemy_health -= double_attack
        print(f"The {enemies[difficulty]['creature']} stumbles and falls! You strike them with a mighty blow!")

    elif 19 >= warrior_initiative != 1 and warrior_initiative > enemy_initiative:






