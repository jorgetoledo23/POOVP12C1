class Item:

    def __init__(self, nombre:str, vida:int, fuerza:int, coste:int):
        self.__Nombre = nombre
        self.__Vida = vida
        self.__Fuerza = fuerza
        self.__Coste = coste

    def getStats(self):
        return f"Coste: [{self.__Coste}] Nombre: [{self.__Nombre}] Vida: [{self.__Vida}] Fuerza: [{self.__Fuerza}]"
    
    def getCoste(self):
        return self.__Coste
    def getVida(self):
        return self.__Vida
    def getFuerza(self):
        return self.__Fuerza
