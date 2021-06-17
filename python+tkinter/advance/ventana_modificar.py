from tkinter import *
from tkinter.messagebox import *
from data_base import *
from ventana_lectura import *
from conexion import *
import control as ct

class Modificar(welcome):

    """clase que presenta la pantalla para modificación de la data de los oficiales"""

    def __init__(self, parent, objeto):    

        self.show = parent
        self.master = Toplevel(self.show)
        self.master.title('Oficiales')
        self.master.geometry('400x220')
        self.titulo = Label(self.master, text="Complete todos los campos solicitados", pady=10)
        self.titulo.grid(row=0,columnspan=5)
        self.objeto = objeto # a la clase Lectura le asigno un nombre/atributo
        self.combo_nombre = ttk.Combobox(self.master,state="readonly", width=18)
        self.combo_rango = ttk.Combobox(self.master,state="readonly", width=18)
        
        # carga de valores (desde base de datos) para combobox nombre
        lista = []
        for x in Oficial.select():
            lista.append(x.nombre)   
        self.combo_nombre["values"] = lista
        self.combo_nombre.bind("<<ComboboxSelected>>", self.seleccion_nombre)

        # carga de valores desde lista "rango" para combobox rango
        rango = ['Almirante', 'Capitán', 'Teniente Comandante','Teniente', 'Teniente Jr.', 'Alferez', 'Alistado', 'Jefe', 'Tripulante']
        self.combo_rango["values"] = rango  
        self.combo_rango.bind("<<ComboboxSelected>>", self.seleccion_rango)      
        
        self.nombre = StringVar()
        self.rango = StringVar()
        self.correo = StringVar()
        
        Label(self.master, text='Oficial:', width=38).grid(row=1, columnspan=3, padx=2, pady=2)
        Label(self.master, text='Nombre').grid(row=2, column=0, padx=2, pady=2)
        self.combo_nombre.grid(row = 2, column = 1, padx=10, pady=2)
        
        Label(self.master, text='Campos a modificar:', width=38).grid(row=3, columnspan=3, padx=2, pady=2)
        Label(self.master, text='Rango').grid(row=4, column=0, padx=2, pady=2)
        self.combo_rango.grid(row = 4, column = 1, padx=10, pady=2)
        Label(self.master, text='Correo').grid(row=5, column=0, padx=2, pady=2)
        Entry(self.master, textvariable = self.correo, width=21).grid(row = 5, column = 1, padx=10)
        
        Button(self.master, text="Actualizar",command=lambda: ct.check2(self, self.objeto, self.nombre,self.rango,self.correo)).grid(row=6, column=0, pady=10, padx=10)
        Button(self.master, text="Volver",command=self.cerrar).grid(row=6, column=1, pady=10, padx=10)

        self.master.grab_set()
        self.master.focus_set()
        self.master.wait_window()

    ### funciones que se ejecutan como métodos por fuera de la clase para mostrar carteles en caso de error o campos vacíos ###

    def asterisco(self,):
        asterisco1 = Label(self.master,text='*', fg='red').grid(row = 4, column = 2, pady=2, sticky=W)
        asterisco2 = Label(self.master,text='*', fg='red').grid(row = 5, column = 2, pady=2, sticky=W)

    def aviso_correo(self,):
        error_correo = Label(self.master)
        error_correo.config(text='name@domain.com', fg='red')
        error_correo.grid(row = 5, column = 2, pady=2, sticky=W)

    ### funciones para la recolecció de los valores en la selección del combobox ###

    def seleccion_nombre(self,evento):
        self.nombre = self.combo_nombre.get()

    def seleccion_rango(self,evento):
        self.rango = self.combo_rango.get()

    def cerrar(self,):
        self.master.destroy()