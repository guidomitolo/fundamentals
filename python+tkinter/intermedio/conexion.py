from data_base import *

"""En este modulo yacen las variables de facil acceso y las funciones necesarias para apelar a la base de datos"""

servidor = "localhost"
usuario = "root"
password = ""
bd = "starfleet"
tabla = "high_command"

def insertar(dato):
    base = database(servidor,usuario,password,bd,tabla)
    base.alta(dato)

def borrar(variable):
    base = database(servidor,usuario,password,bd,tabla)
    base.delete(variable)

def leer():
    base = database(servidor,usuario,password,bd,tabla)
    return base.leer()