from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from oficiales import *
import conexion as cx
from ventana_carga import *
from ventana_modificar import *

def advertencia(ventana, valor):

    if valor == 1:
        ventana.aviso_fecha()
        historial('Ingreso de fecha incorrecto')
    elif valor == 2:
        ventana.aviso_correo()
        historial('Ingreso de correo incorrecto')

def check(ventana, objeto, nombre, fecha, raza, rango, correo, sector):

    if nombre.get() == '' or fecha.get() =='' or correo.get() == '':
        showwarning("Error",'Completar los campos vacíos')
    else:
        oficial = Persona(nombre=nombre.get(),raza=raza,fecha=fecha.get(),rango=rango,correo=correo.get(),sector=sector)
        nacimiento = oficial.validación_fecha()
        if nacimiento == 1:
            showerror('Error','Formato de fecha incorrecto')
            advertencia(ventana=ventana, valor=nacimiento)
        else:
            email = oficial.validación_mail()
            if email == 2:
                showerror('Error','Formato de email incorrecto')
                advertencia(ventana=ventana, valor=email)
            else:
                dato = oficial.cargadatos()
                cx.insertar(dato, objeto, ventana) # paso el dato formateado por la clase oficial, más la clase Lectura

def check2(ventana, objeto, nombre, rango, correo):
    point = 0
    if isinstance(nombre, StringVar) == True:
        showwarning("Error",'Seleccione un oficial')
    else:
        try:
            rango
        except AttributeError:
            point = 1
        if point == 1:
            showwarning("Error",'Completar los campos vacíos')
            ventana.asterisco()
        else: 
            if correo.get() == '':
                showwarning("Error",'Completar los campos vacíos')
                ventana.asterisco()
            else:
                oficial = Persona(nombre=nombre,rango=rango,correo=correo.get())
                email = oficial.validación_mail()
                if email == 2:
                    showerror('Error','Wrong email format')
                    advertencia(ventana, email)
                else:
                    ventana.cerrar()                
                    dato = oficial.cargadatos()
                    cx.update(dato, objeto, ventana) # paso el dato formateado por la clase oficial, más la clase Lectura