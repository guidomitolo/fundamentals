import re
from tkinter import *
from tkinter.messagebox import *
from conexion import *
import ventana_carga

class Persona:
    """ esta clase está destinada a instanciar en una tupla cada oficial ingresado al sistema, previamente verificado los campos ingresados. La tupla servirá para subir la info a la bd"""
    def __init__(self, nombre, raza, fecha, rango, correo):
        self.nombre = nombre
        self.raza  = raza
        self.fecha = fecha
        self.rango = rango
        self.correo = correo
    
    def __str__(self):
        return 'Nombre: {0}\nRaza: {1}\nFecha: {2}\nRango: {3}\nCorreo: {4}'.format(self.nombre, self.raza, self.fecha, self.rango, self.correo)

    def validación_fecha(self):
        patron = re.compile(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$')
        control = patron.search(self.fecha)
        try:
            return control.group()
        except AttributeError:
            return 1

    def validación_mail(self):
        patron = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z0-9]{1,3}.[a-z0-9]{1,2}$')
        control = patron.search(self.correo)
        try:
            return control.group()
        except AttributeError:
            return 2

    def cargadatos(self):
        datos = (self.nombre, self.raza, self.fecha, self.rango, self.correo)
        return datos