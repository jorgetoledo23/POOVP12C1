#Sistema de dos Turnos!
import os
from Model.Personaje import *
import Tienda

turno = 1
Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")
Ganador = None
while True:
    os.system("cls")

    print("Stats Jugadores: \n")

    print(Player1.getStats())
    print(f"Inventario Jugador 1: {Player1.getInventario()}\n")

    print(Player2.getStats())
    print(f"Inventario Jugador 2: {Player2.getInventario()}\n")


    print(f"Turno Actual Jugador: {turno} \n")

    print("[1] - Atacar")
    print("[2] - Comprar Item")
    print("[3] - Vender Item")

    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":
        if turno == 1: 
            Player1.Atacar(Player2)
            if Player2.getVida() <= 0:
                Ganador = Player1
        else: 
            Player2.Atacar(Player1)
            if Player1.getVida() <= 0:
                Ganador = Player2
    
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

    if opcion == "3":
        os.system("cls")
        if turno == 1:
            indice = 1
            for item in Player1.getListaInventario():
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            seleccion = int(input("\nQue Item quieres Vender?: "))
            Player1.Vender(Player1.getListaInventario()[seleccion - 1])
        else: 
            indice = 1
            for item in Player2.getListaInventario():
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            seleccion = int(input("\nQue Item quieres Vender?: "))
            Player2.Vender(Player2.getListaInventario()[seleccion - 1])


    if Ganador == None:
        pass
    else:
        print(f"El ganador es: {Ganador.getStats()}")
        break

    input("Turno terminado. Presiona Enter para Continuar!")

    if turno == 1: turno = 2
    else: turno = 1

