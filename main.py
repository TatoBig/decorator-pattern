from azazel import Azazel
from bethany import Bethany
from fighter_decorator import FighterDecorator
from isaac import Isaac
from judas import Judas
from holy_mantle_decorator import   HolyMantleDecorator
from brimstone_decorator import BrimstoneDecorator
from fighter import Fighter
from time import sleep


def choose_character() -> Fighter:
    fighter_selected: Fighter = None
    print("----------------------------------------------------")
    print("1. Isaac")
    print("2. Bethany")
    print("3. Azazel")
    print("4. Judas")
    fighter = int(input("Porfavor escoja una opcion: "))
    if fighter == 1:
        fighter_selected = Isaac()
    if fighter == 2:
        fighter_selected = Bethany()
    if fighter == 3:
        fighter_selected = Azazel()
    if fighter == 4:
        fighter_selected = Judas()
    return fighter_selected

def choose_item(fighter: Fighter) -> Fighter:
    item_selected = None
    print("-----------------------")
    print("2. holy mantle")
    print("3. brimstone")
    item_virtual = int(input("Escoga su arma: "))
    if item_virtual == 2:
        item_selected = HolyMantleDecorator(fighter)
    if item_virtual == 3:
        item_selected = BrimstoneDecorator(fighter)
    return item_selected           

def game():
    player1: Fighter = None
    player2: Fighter = None

    option: int = 0
    while(option != 4):
        print("-----------------------------------------------------")
        print("1. Seleccionar personajes")
        print("2. Equipar objetos")
        print("3. Pelear!")
        print("4. Salir")
        option = int(input("Porfavor marque el numero de la opcion: "))
        if option == 1:
            print("+++++++++++++++++++++++++++++++++++++++++++")
            print("Seleccionar personajes")
            if player1 == None:
                print("Selección del jugador 1")
                player1 = choose_character()
            if player2 == None:
                print("Selección del jugador 2")
                player2 = choose_character()
        elif option == 2:
            if player1 != None and player2 != None:
                print("+++++++++++++++++++++++++++++++++++++++++++")
                print("1. Equipar personaje del jugador 1")
                print("2. Equipar personaje del jugador 2")
                item_option = int(input("Porfavor marque el numero de la opcion: "))
                if item_option == 1:
                    player1 = choose_item(player1)
                if item_option == 2:
                    player2 = choose_item(player2)
            else:
                print("Primero debe seleccionar personajes a los jugadores")
        elif option == 3:
            player1_attack_cooldown = 0
            player2_attack_cooldown = 0
            while player1.get_hp() > 0 and player2.get_hp() > 0:
                sleep(0.5)
                if player1.get_speed() <= player1_attack_cooldown:
                    damage = player1.compute_damage(player2)
                    print(f"Jugador 1 ataca haciendo {damage} puntos de daño")
                    player2.reduce_hp(damage)
                    print(f"Jugador 1 HP: {player1.get_hp()}")
                    player1_attack_cooldown = 0
                else: 
                    player1_attack_cooldown += 1
                if player2.get_speed() <= player2_attack_cooldown:
                    damage = player2.compute_damage(player1)
                    print(f"Jugador 2 ataca haciendo {damage} puntos de daño")
                    player1.reduce_hp(damage)
                    print(f"Jugador 2 HP: {player2.get_hp()}")
                    player2_attack_cooldown = 0
                else: 
                    player2_attack_cooldown += 1
            if player1.get_hp() <= 0:
                print("Gana jugador 2")
            if player2.get_hp() <= 0:       
                print("Gana jugador 1")

            player1 = None
            player2 = None


if __name__ == '__main__':
    game()