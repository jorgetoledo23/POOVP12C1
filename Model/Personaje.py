# Crear una class Personaje que tenga un atributo 
# Nombre, Vida, Fuerza y Oro

# El nombre del personaje debe ser proporcionado por el usuario
# Pero su Vida y Fuerza comenzar en 100 y su Oro en 1000

# Crear 2 personajes y mostrar sus Stats

class Personaje:

    def __init__(self, nombre):
        pass

    def getStats(self):
        pass

Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")


print(Player1.getStats())
print(Player2.getStats())