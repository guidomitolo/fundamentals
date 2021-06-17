#! python3
from tkinter import *
from ventana_lectura import *
from observador import *
import os

class welcome(admin):

    """clase de recepción e ingreso a la app principal (heredera de una clase del modulo observador)"""

    def __init__(self, root):
        
        self.intro = root
        self.intro.title("Starfleet Database")
        my_path = os.path.dirname(__file__)
        photo = PhotoImage(file="{0}/starfleet.gif".format(my_path))
        label = Label(self.intro)
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0,columnspan=4)
        Label(self.intro, text="High Command Personnel",padx=10, pady=10, relief=RAISED,width=38).grid(row=1, columnspan=4, padx=5, pady=5)
        Button(self.intro, text='Ingresar',command=self.ingreso).grid(row=2,column=1)
        Button(self.intro, text='Salir', command= self.salida).grid(row=2,column=2)

        afi_uno = espia_uno(self) # se instancia el observador, que toma como parámetro la clase instanciada "welcome"
        afi_dos = espia_dos(self)

        self.intro.grab_set()
        self.intro.focus_set()
        self.intro.wait_window()
    
    def salida(self,):
        self.intro.destroy()

    def ingreso(self):
        aplicacion = Lectura(self.intro)
        aplicacion.pantalla()
    
if __name__ == '__main__':

    root = Tk()
    app = welcome(root)
    root.mainloop() 
