from tkinter import *
from tkinter.messagebox import *
import ventana_lectura
import conexion
from log_creator import *

lista = []

def seleccion(var,fila,resultado):
    """esta función permite cruzar la selección de cada checkboxe con su correspondiente registro y guardarlos en una lista"""
    if var == 1:
        lista.append(resultado[fila][1])
    else:
        lista.remove(resultado[fila][1])
        
def erase(ventana):
    """esta función recorre y elimina cada uno de los valores de la lista de registros creada por la función 'selección"""
    if lista == []:
        showwarning("Error",'Primero seleccione un oficial')
    else:
        num = 0
        while lista != []:
            conexion.borrar(lista[-1])
            lista.remove(lista[-1])
            num +=1
        showwarning("Eliminación",f'Se han borrado {num} registros')
        historial('Se ha borrado un registro')
        ventana_lectura.recargar(ventana)