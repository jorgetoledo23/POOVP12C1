#Identificar y generar los modelos de clases para crear un sistema que administre un taller mecanico.
#Es decir, las reparaciones que en este se generan, los repuestos que se utilizan, los autos que ingresan 
#los mecanicos que hacen las reparaciones y los clientes a los que se atienden.

class Reparacion:
    fecha = ""
    codigo = ""
    cliente = ""
    mecanico = ""
    auto = ""
    observacion = ""
    repuestos = ""
    valor = ""

class Cliente:
    rut = ""
    nombres =""
    apellidos =""
    direccion =""
    comuna =""
    telefono = ""
    correo =""

class Mecanico:
    rut = ""
    nombres =""
    apellidos =""
    direccion =""
    comuna =""
    telefono = ""
    correo =""

class Auto:
    patente =""
    modelo =""
    marca =""
    vim = ""
    color = ""
    año = ""
    dueño = ""

class Repuesto:
    codigo = ""
    nombre =""
    marca =""
    valor =""





