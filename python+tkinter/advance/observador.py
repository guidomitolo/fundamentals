import sys # se agrega esta libreria para ejecutrar el método __getframe()
from datetime import *

def notificar(entry):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S ")
    archivo = open('obs_records.txt', 'a')
    archivo.write(timestamp)
    archivo.write(entry)
    archivo.write('\n')
    archivo.close()

class admin:

    """ la clase admin gestiona a los obseradores = lleva un registro de sus apariciones y ejecuta las funciones
    que les son propias a cada uno de ellos"""

    espias = []
    
    def agregar(self, obj): # "obj" es igual a la instancia del espía y "self" es la instancia de admin en welcome
        
        """esta función imprime advertencia y completa la lista 'espias'"""
        
        self.espias.append(obj)
        notificar(f'Ha ingresado el observador {obj} a {self}')
                
    def realizar(self,):

        """esta función ejecuta el método update, distinguiendo el observador y la función desde donde fue llamada"""

        funcion = sys._getframe().f_back.f_code.co_name # esto me permite distinguir la función puntual del objeto donde fue llamado el método "realizar"
        if type(self).__name__ == 'Lectura':
            espia_uno.update(self, funcion)
        else:
            espia_dos.update(self)

class espia_uno():

    """esta clase notifica el cambio de estilo de la app y la eliminación de un oficial de la base de datos"""

    def __init__(self, obj):
        self.espia_uno = obj
        self.espia_uno.agregar(self) # cuando se instancia el observador, se ejecuta el método agregar (de la clase admin, instanciada por welcome)
        self.id = self

    def update(self, funcion):
        if funcion == 'estilo': # según el nombre la función, la respuesta es distinta
            entry = 'El observador espia_uno ha detectado un cambio en el color de la app'
            notificar(entry)
        else:
            entry = 'El observador espia_uno ha detectado la eliminación de un registro'
            notificar(entry)

class espia_dos():

    """esta clase notifica el registro y la modificación de un oficial en la base de datos"""

    def __init__(self, obj):
        self.espia_dos = obj
        self.espia_dos.agregar(self) # cuando se instancia el observador, se ejecuta el método agregar (de la clase admin, instanciada por welcome)
    
    def update(self):
        if type(self).__name__ == 'Modificar':
            entry = 'El observador espia_dos ha detectado la actualización de un registro'
            notificar(entry)
        else:
            entry = 'El observador espia_dos ha detectado la carga de un nuevo registro'
            notificar(entry)