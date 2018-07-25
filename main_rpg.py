from character_lib import *


enemies = [goblin, medic, shadow, wizard, zombie]


def choose_enemy():
    
    print('Choose an enemy to fight!')
    for i in range(len(enemies)):
        print(i+1, enemies[i].race)
    while(True):   
        try:
            enemy = enemies[(int(input("> "))-1)]
        except IndexError:
            print("Invalid input, please choose between 1 and 5")
            continue
        else:
            if enemy in enemies:
                hero.attack(enemy)
                battle(enemy)
            else:
                print("Invalid input {}".format(input))

            
def battle(enemy):
    while hero.alive() and enemy.alive():
        print('Hero: {} {}: {}'.format(hero.health, enemy.race ,enemy.health))
        print("""What now?
            1. Strike again!
            2. Do nothing
            3. Flee!""")
        print("> ", end=' ')
        keyinput = int(input())
        if keyinput == 1:
            hero.attack(enemy)
            
        elif keyinput == 2:
            pass
        elif keyinput == 3:
            print("coward!")
            main_menu()
        else:
            print("Invalid input. Please choose between 1 and 3")
    main_menu()

def main_menu():
    while(True):
        print("""What do you want to do?
            1. Do battle
            2. Go shopping
            3. View my stats
            0. Exit game""")
        try:
            keyinput = int(input())
        except ValueError:
            print("Invalid input, please choose between 1 and 3 or 0")
            continue
        else:
            if keyinput == 1:
                choose_enemy()
            elif keyinput == 2:
                store.shop(hero)
                main_menu()

            elif keyinput == 3:
                hero.status()
                main_menu()
            elif keyinput == 0:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input, please choose between 1 and 3 or 0")


main_menu()
