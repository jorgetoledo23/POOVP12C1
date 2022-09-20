#Sistema de dos Turnos!
import os
from Model.Personaje import *
import Tienda

turno = 1
Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")
while True:
    os.system("cls")

    print("Stats Jugadores: \n")

    print(Player1.getStats())
    print(Player2.getStats())

    print(f"Turno Actual Jugador: {turno} \n")

    print("[1] - Atacar \n")
    print("[2] - Comprar Item \n")

    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":
        if turno == 1: 
            Player1.Atacar(Player2)
        else: 
            Player2.Atacar(Player1)
    
    if opcion == "2":
        os.system("cls")
        indice = 1
        for item in Tienda.Tienda:
            print(f"[{indice}] - {item.getStats()}")
            indice += 1
        seleccion = int(input("\nQue Item quieres comprar?: "))
        if turno == 1:
            Player1.Comprar(Tienda.Tienda[seleccion - 1])
        else: Player2.Comprar(Tienda.Tienda[seleccion - 1])
        print("Item Comprado!")

    print("Turno terminado. Presiona Enter para Continuar!")

    if turno == 1: turno = 2
    else: turno = 1