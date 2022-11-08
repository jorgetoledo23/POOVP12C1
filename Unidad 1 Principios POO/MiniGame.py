#Sistema de dos Turnos!
import os
from Model.Personaje import *
import Tienda

turno = 1
Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")
Ganador = None
JugadorTurno = Player1
JugadorEspera = Player2

while True:
    os.system("cls")
    TurnoExitoso = True
    print("Stats Jugadores: \n")

    print(Player1.getStats())
    print(f"Inventario Jugador 1: {Player1.getInventario()}\n")

    print(Player2.getStats())
    print(f"Inventario Jugador 2: {Player2.getInventario()}\n")


    print(f"Turno Actual Jugador: {turno} \n")

    print("[1] - Atacar")
    print("[2] - Comprar Item")
    print("[3] - Vender Item")
    print("[4] - Rendirte")

    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":
        JugadorTurno.Atacar(JugadorEspera)
        if JugadorEspera.getVida() <= 0:
            Ganador = JugadorEspera
    
    if opcion == "2":
        os.system("cls")     
        if len(JugadorTurno.getListaInventario())>=6:
            print("Tu Inventario esta completo!")
            TurnoExitoso = False
        else:
            indice = 1
            for item in Tienda.Tienda:
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            seleccion = 0
            while seleccion<=0 or seleccion>=len(Tienda.Tienda):
                print("Item Incorrecto!")
                seleccion = int(input("\nQue Item quieres comprar?: "))
            
            JugadorTurno.Comprar(Tienda.Tienda[seleccion - 1])
        input("Presiona Enter para Continuar.")


    if opcion == "3":
        os.system("cls")
        indice = 1
        for item in JugadorTurno.getListaInventario():
            print(f"[{indice}] - {item.getStats()}")
            indice += 1
        seleccion = int(input("\nQue Item quieres Vender?: "))
        JugadorTurno.Vender(JugadorTurno.getListaInventario()[seleccion - 1])

    if opcion == "4":
        confirmacion = input("Estas seguro de Rendirte? (S/N)")
        if confirmacion == "S":
            Ganador = JugadorEspera
        else:
            TurnoExitoso = False

    if Ganador != None:
        print(f"El ganador es: {Ganador.getStats()}")
        break

    if TurnoExitoso:
        input("Turno terminado. Presiona Enter para Continuar!")
        if turno == 1: 
            turno = 2
            JugadorTurno = Player2
            JugadorEspera = Player1
        else: 
            turno = 1
            JugadorTurno = Player1
            JugadorEspera = Player2

