#! python3
from tkinter import *
from ventana_carga import *
import random

class welcome():
    """esta clase consiste en darle la bienvenida al usuario antes de ingresar a la app propiamente dicha"""
    def __init__(self, parent, tabula):
       
        self.parent = parent
        self.cuadro = tabula
        parent.title("Starfleet Database")
        photo = PhotoImage(file="inter\starfleet.gif")
        label = Label(self.parent)
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0,columnspan=4)
        Label(self.parent, text="High Command Personnel",padx=10, pady=10, relief=RAISED,width=38).grid(row=1, columnspan=4, padx=5, pady=5)
        Button(self.parent, text='Enter',command= lambda: inside(parent,tabula)).grid(row=2,column=1)
        Button(self.parent, text='Exit', command= lambda: parent.destroy()).grid(row=2,column=2)

if __name__ == '__main__':

    header = 'Nombre','Raza','Fecha de Nacimiento','Rango', 'Correo'
    root = Tk()
    welcome(root, header)
    root.mainloop() 