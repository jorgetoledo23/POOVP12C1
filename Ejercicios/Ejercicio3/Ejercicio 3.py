from msilib.schema import Class


class Dueno:
    Rut = ""
    Nombre = ""
    Apellidos = ""


class Auto:
    Patente = ""
    Marca = ""
    Modelo = ""
    Año = ""
    Color = ""
    Dueño = ""


#A las dos clases anteriores:
#1-Generar sus respectivos constructores solicitando todos los atributos de cada class
#2-Validar en la clase cliente que Rut, Nombre y Apellido sean obligatoriamente de tipo cadena de texto (str)
#3-Validar en la clase Auto que el atributo dueño sea obligatoriamente de tipo Dueno