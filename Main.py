from Model.Clases import *
from Model.Venta import *
#Instancia => Ocurrencia de una class
#Al generar una Instancia (espacion en memoria) pasa a ser un Objeto
#Objeto

C = Cliente() #=> Objeto
C.Rut = "1.111.111-1"
C.Nombre = "Arturo"
C.Apellido = "Vidal"
C.Edad = 23

C1 = Cliente()
C1.Rut = input("Ingresa Rut: ")
C1.Nombre = input("Ingresa Nombre: ")
C1.Apellido = input("Ingresa Apellido: ")
C1.Edad = input("Ingresa Edad: ")

Venta1 = Venta()
Venta1.Fecha = "23/08/2022"
Venta1.Codigo = "1234532"
Venta1.Articulos = [] #Listado de Productos
Venta1.Caja = 10
Venta1.Sucursal = "Lider Express Curico"
Venta1.TipoPago = "Efectivo"
Venta1.Cliente = C
