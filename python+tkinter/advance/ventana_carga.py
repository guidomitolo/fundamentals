from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd
from control import *
from conexion import *
from PIL import Image, ImageTk
from intro import *
import os

class Carga(welcome):

    """clase que presenta la pantalla de carga de datos"""

    def __init__(self, parent, objeto):

        self.show = parent
        self.master = Toplevel(self.show)
        self.master.title('Oficiales')
        self.entries = Frame(self.master,padx=2,pady=2,relief=RAISED, borderwidth=1)
        self.entries.pack(side=LEFT)
        self.carnet = Frame(self.master,padx=2,pady=2,relief=RAISED, borderwidth=1)
        self.carnet.pack(side=RIGHT)
        self.objeto = objeto # a la clase Lectura le asigno un nombre/atributo

        Label(self.entries, text="Complete todos los datos campos solicitados", pady=10).grid(row=0,columnspan=5)
        cuadro = 'Nombre','Raza','Fecha de Nacimiento','Rango', 'Correo', 'Sector'
        for fila in range(len(cuadro)):
            self.item = Label(self.entries, text=cuadro[fila])
            self.item.grid(row=fila+1, column=0, padx=2, pady=2)
    
        self.nombre = StringVar()
        self.combo_uno = ttk.Combobox(self.entries,state="readonly", width=15)
        self.fecha = StringVar()
        self.combo_dos = ttk.Combobox(self.entries,state="readonly", width=15)
        self.correo = StringVar()
        self.combo_tres = ttk.Combobox(self.entries,state="readonly", width=15)

        raza = ['Bajorana', 'Borg','Ferengi','Humana','Klingon','Vulcana','Andoriana', 'Romulana','Androide']
        rango = ['Almirante', 'Capitán', 'Teniente Comandante','Teniente', 'Teniente Jr.', 'Alferez', 'Alistado', 'Jefe', 'Tripulante']
        sector = ['Cuadrante Alpha','Cuadrante Beta','Cuadrante Gamma' ,'Cuadrante Delta']

        self.combo_uno["values"] = raza
        self.combo_dos["values"] = rango
        self.combo_tres["values"] = sector
        self.combo_uno.bind("<<ComboboxSelected>>", self.seleccion_raza)
        self.combo_dos.bind("<<ComboboxSelected>>", self.seleccion_rango)
        self.combo_tres.bind("<<ComboboxSelected>>", self.seleccion_sector)

        e1 = Entry(self.entries, textvariable = self.nombre, width=18).grid(row = 1, column = 1, padx=10, pady=2)
        self.combo_uno.grid(row = 2, column = 1, padx=10, pady=2)
        e2 = Entry(self.entries, textvariable = self.fecha, width=18).grid(row = 3, column = 1, padx=10, pady=2)
        self.combo_dos.grid(row = 4, column = 1, padx=10, pady=2)
        e3 = Entry(self.entries, textvariable = self.correo, width=18).grid(row = 5, column = 1, padx=10, pady=2)
        self.combo_tres.grid(row = 6, column = 1, padx=10, pady=2)

        # además del objeto de la clase Lectura, paso el objeto de esta misma clase para que se ejecuten los métodos de los avisos en etiquetas
        Button(self.entries, text="Alta", command=self.filtro).grid(row=7, column=0, pady=10, padx=10)
        Button(self.entries, text="Volver", command=self.cerrar).grid(row=7, column=1, pady=10, padx=10)
        
        self.master.grab_set()
        self.master.focus_set()
        self.master.wait_window()

    def cargar_foto(self,nombre):
        """función que abre ventana para almacenar ruta de imagenes"""
        if askyesno('Imagen','¿Desea cargar una foto carné?'):
            carpeta = 'img/'
            pic = fd.askopenfile(initialdir= "/img", title="Elija foto carné")
            fuente = carpeta + os.path.basename(pic.name)
            img = Image.open(fuente)
            photo_image = ImageTk.PhotoImage(img)
            upload(nombre,fuente)
            self.cerrar()
        else:
            self.cerrar()

    def filtro(self,):
        """función de control de los combobox, de quedar vacíos (vacío = attributeerror)"""
        point = 0
        try:
            self.rango
        except AttributeError:
            point = 1
        try:
            self.raza
        except AttributeError:
            point = 1
        try:
            self.sector
        except AttributeError:
            point = 1
        if point == 0:
            check(ventana=self,objeto=self.objeto,nombre=self.nombre,raza=self.raza,fecha=self.fecha,rango=self.rango,correo=self.correo,sector=self.sector)
        else:
            showwarning("Error",'Completar los campos vacíos')

    ### funciones para la recolecció de los valores en la selección del combobox ###

    def seleccion_raza(self,evento):
        self.raza = self.combo_uno.get()

    def seleccion_rango(self,evento):
        self.rango = self.combo_dos.get()
    
    def seleccion_sector(self,evento):
        self.sector = self.combo_tres.get()

    ### funciones que se ejecutan como métodos por fuera de la clase para mostrar carteles en caso de error o campos vacíos ###

    def aviso_fecha(self,):
        error_fecha = Label(self.entries)
        error_fecha.config(text='dd/mm/aaaa', fg='red')
        error_fecha.grid(row = 3, column = 2, padx=2, pady=2, sticky=W)

    def aviso_correo(self,):    
        error_correo = Label(self.entries)
        error_correo.config(text='name@domain.com', fg='red')
        error_correo.grid(row = 5, column = 2, padx=2, pady=2, sticky=W)
    
    def cerrar(self,):
        self.master.destroy()