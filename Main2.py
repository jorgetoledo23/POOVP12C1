class Cliente:
    #Atributos => Caracteticas en comun de todo los Clientes
    Rut = ""
    Nombre = ""
    Apellido = ""
    Edad = 0
    
    #Metodo Constructor
    def __init__(self, rut, nombres, apellidos):
        self.Rut = rut

        lista = str(nombres).split(" ")
        newName = ""
        for val in lista:
            newName += val.capitalize() + " "

        lista = str(apellidos).split(" ")
        newApe = ""
        for val in lista:
            newApe += val.capitalize() + " "

        self.Nombre = newName
        self.Apellido = newApe

class Encomienda:
    Id = None
    Direccion = None
    Cliente = None

    def __init__(self, id, dir, cliente):
        if not isinstance(id, int): # "asdas"
            raise TypeError("El Codigo de la Encomienda debe ser un numero entero!")
        if not isinstance(cliente, Cliente):
            raise TypeError("El Cliente, debe ser de tipo Cliente")
        
        self.Id = id
        self.Direccion = dir
        self.Cliente = cliente

C = Cliente("1.111.111-1", "arTURo aLexIS", "viDAL SanCHEZ")

print(f"Rut: {C.Rut}")
print(f"Nombres : {C.Nombre}")
print(f"Apellidos : {C.Apellido}")

E = Encomienda(123456789, "Prat 500, Curico", C)