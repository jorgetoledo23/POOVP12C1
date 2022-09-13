#Sistema de dos Turnos!
import os
from Model.Personaje import *

turno = 1
Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")
while True:
    os.system("cls")

    print("Stats Jugadores: \n")

    print(Player1.getStats())
    print(Player2.getStats())

    print(f"Turno Actual Jugador: {turno}")
    print("[1] - Atacar")
    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":
        if turno == 1: 
            Player1.Atacar(Player2)
        else: 
            Player2.Atacar(Player1)

    print("Turno terminado. Presiona Enter para Continuar!")

    if turno == 1: turno = 2
    else: turno = 1