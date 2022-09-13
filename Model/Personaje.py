# Crear una class Personaje que tenga un atributo 
# Nombre, Vida, Fuerza y Oro

# El nombre del personaje debe ser proporcionado por el usuario
# Pero su Vida y Fuerza comenzar en 100 y su Oro en 1000

# Crear 2 personajes y mostrar sus Stats

import os
os.system("cls")
class Personaje:

    def __init__(self, nombre):
        self.__Nombre = nombre
        self.__Vida = 100
        self.__Fuerza = 100
        self.__Oro = 1000

    def getStats(self):
        return f"Nombre: {self.__Nombre}\nVida: {self.__Vida}\nFuerza: {self.__Fuerza}\nOro: {self.__Oro}\n"

    def getVida(self):
        return self.__Vida

    def setVida(self, nuevaVida:int):
        self.__Vida = nuevaVida


    def Atacar(self, Objetivo):
        poderGolpe = self.__Fuerza / 15 + 10
        nuevaVida = Objetivo.getVida() - poderGolpe
        Objetivo.setVida(nuevaVida)






