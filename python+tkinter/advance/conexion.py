from log_creator import *
from data_base import *
from ventana_lectura import *
from tkinter.messagebox import *
from peewee import *

"""el modulo presenta cuatro funciones que tienen acceso externo al módulo que administra la base de datos
todas las funciones estan adornadas con un decorador que registra su en un txt su ejecución"""
 
@historial
def insertar(dato, objeto, ventana): # el objeto me sirve para ejecutar el método pantalla sin llamar a la clase Lectura
    oficial = Oficial()
    oficial.nombre=dato[0]
    oficial.raza=dato[1]
    oficial.fecha=dato[2]
    oficial.rango=dato[3]
    oficial.correo=dato[4]
    oficial.sector=dato[5]
    try:
        oficial.save()
        ventana.cargar_foto(dato[0])
        ventana.realizar()
        objeto.pantalla()
    except IntegrityError:
        showwarning('Error', 'El nombre de usuario ya figura en la base de datos')

@historial
def erase(nombre, objeto):
    oficial = Oficial()
    try:
        query = Oficial.select().where(Oficial.nombre == nombre).get()
        query.delete_instance()
        showinfo('Suprimir', "El oficial {0} se ha elimado con éxito de la base de datos".format(nombre))
        objeto.realizar()
        objeto.pantalla()
    except:
        showerror('Error','No existe el oficial')

@historial
def update(dato, objeto, ventana):
    oficial = Oficial()
    try:
        query = (Oficial
        .update(rango=dato[1], correo=dato[2])
        .where((Oficial.nombre == dato[0]))
        .execute())
        showinfo('Modificación','Los datos del usuario se han modificado')
        ventana.realizar()
        objeto.pantalla()
    except:
        showerror('Error','No existe el oficial')

@historial
def upload(nombre, imagen):
    oficial = Oficial()
    query = (Oficial
    .update(foto=imagen)
    .where(Oficial.nombre == nombre)
    .execute())
    showinfo('Imagen','Usted ha cargado una imagen')
