from tkinter import *
from conexion import *
from tkinter.messagebox import *
from delete import *
from log_creator import *

class Lectura():
    """Esta clase está destinada desplegar mediante un cuadro de doble entrada en una ventana de tkinter todos los registros previamente cargados por la aplicación en mysql"""
    def __init__(self, parent):
        self.inside=Toplevel()
        self.inside.title("Alpha Sector Crew")
        self.var = [] # futura lista de variables para checkbutton
        resultado = leer()
        try:
            for fila in range(len(resultado)): # filas (tuplas = oficial)
                for columna in range(len(resultado[fila])): # columnas (valores de tuplas = atributos de un oficial)
                    celda = StringVar()
                    celda.set(resultado[fila][columna])
                    Label(self.inside, text=header[columna]).grid(row=1,column=columna)
                    Entry(self.inside, textvariable=celda).grid(row=fila+2,column=columna) # en c/celda se ubica el contenido obtenido de resultado [x][y]
                self.var.append(IntVar())
                self.var[-1].set(0) # c/nueva variable agregada se acomoda al inicio de la lista
                Checkbutton(self.inside, text=fila+1,variable=self.var[-1], command=lambda fila=fila: seleccion(self.var[fila].get(),fila,resultado)).grid(row=fila+2,column=6)
        except TypeError:
            showwarning('No hay registros cargados','Primero ingrese un oficial')

        Button(self.inside, text='Actualizar', command=lambda:recargar(self.inside)).grid(row=fila+4, column=1)
        Button(self.inside, text="Eliminar", command=lambda:erase(self.inside)).grid(row=fila+4, column=3, pady=2, padx=2)

        menubar = Menu(self.inside)
        menuFile = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=menuFile)
        menuFile.add_command(label="Exit",command=lambda:self.inside.destroy())
        self.inside.config(menu=menubar)

        self.inside.grab_set()
        self.inside.focus_set()
        self.inside.wait_window()

def recargar(ventana):
    """ esta función está destinada a recargar la clase Lectura cada vez que se oprime el botón Actualizar o cada vez que se elimina un registro"""
    registros = leer() # revisa si hay registros en mysql
    if registros == []:
        showwarning('La base de datos se ha vaciado','Vuelva a cargar un oficial')
        ventana.destroy()
        historial('Vista de base de datos fallida: se han borrado todos los registros')
    else:
        ventana.destroy()
        Lectura(ventana)
        historial('Actualización a base de datos')
    
    """
    try:
        ventana.destroy()
        Lectura(ventana)
    except UnboundLocalError:
        showwarning('No hay registros cargados','Debe volver a cargar un oficial')
        ventana.destroy()"""