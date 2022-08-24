#============ Class ============== 

#Plantilla que representa las caracteristicas (Atributos) y comportamiento (Metodos)
#que tendran todos los Objetos creados a partir de ella.
#Establece la estructura que debe tener un objeto


class Cliente:
    #Atributos => Caracteticas en comun de todo los Clientes
    Rut = None
    Nombre = ""
    Apellido = ""
    Edad = 0
    

    #Metodos => Comportamiento en comun de todos los Cliente
    def obtenerNombreCompleto(self):
        return f"Nombre: {self.Nombre}, Apellido: {self.Apellido}"



class Animal:
    #Atributos
    Especie = ""
    Habitat = ""
    NombreComun = ""
    NombreCientifico = ""
    esPeligroExtincion = None
    urlImagen = None


    #Metodos
    def EmitirSonido(self):
        pass



class SmartPhone:
    pass