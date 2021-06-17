from tkinter import *
from tkinter.messagebox import *
from ventana_lectura import *
from ventana_estilo import *
from oficiales import *
from log_creator import *
from conexion import *

class inside():

    """esta clase está creada a fin de que el humano pueda cargar los datos de los oficiales en la base de datos web de mysql a través de una interface más amigable en tkinter"""

    def __init__(self, parent=NONE, tabula=NONE):    

        self.master = Toplevel()
        self.master.title('Officers')
        self.master.geometry('400x220')
        self.cuadro = tabula
        self.titulo = Label(self.master, text="Please enter Officer's Data", pady=10)
        self.titulo.grid(row=0,columnspan=5)
 
        for fila in range(len(self.cuadro)):
            self.item = Label(self.master, text=self.cuadro[fila])
            self.item.grid(row=fila+1, column=0, padx=2, pady=2)
        
        self.nombre = StringVar()
        self.raza = StringVar()
        self.fecha = StringVar()
        self.rango = StringVar()
        self.correo = StringVar()

        e1 = Entry(self.master, textvariable = self.nombre).grid(row = 1, column = 1, padx=10, pady=2)
        e2 = Entry(self.master, textvariable = self.raza).grid(row = 2, column = 1, padx=10, pady=2)
        e3 = Entry(self.master, textvariable = self.fecha).grid(row = 3, column = 1, padx=10, pady=2)
        e4 = Entry(self.master, textvariable = self.rango).grid(row = 4, column = 1, padx=10, pady=2)
        e5 = Entry(self.master, textvariable = self.correo).grid(row = 5, column = 1, padx=10, pady=2)

        Button(self.master, text="Alta", command=self.control).grid(row=fila+2, column=0, pady=10, padx=2)
        Button(self.master, text="Registro",command=self.registro).grid(row=fila+2, column=1, pady=10, padx=2)

        menubar = Menu(self.master)
        menuFile = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=menuFile)
        menuFile.add_command(label="Estilo", command=self.estilo)
        menuFile.add_command(label="Exit",command=lambda:self.master.destroy())
        menubar.add_command(label="Help", command=self.help)
        self.master.config(menu=menubar)
        
        self.master.grab_set()
        self.master.focus_set()
        self.master.wait_window()

    def estilo(self):
        """esta método le permite al humano cambiar el color de fondo de la ventana y los widgets"""
        clave = color()
        self.master.config(bg=clave)
        self.titulo.config(bg=clave)
        self.item.config(bg=clave)

    def registro(self):
        registros = leer() # revisa si hay registros en mysql
        if registros == []:
            showwarning('No hay registros cargados','Primero ingrese un oficial')
            historial('Vista de base de datos fallida: no hay datos cargados')
        else:
            ventana = Lectura(self.master)
            historial('Acceso a base de datos')

    def advertencia(self, valor):
        if valor == 1:
            error_fecha = Label(self.master)
            error_fecha.config(text='dd/mm/aaaa', fg='red')
            error_fecha.grid(row = 3, column = 2, padx=2, pady=2, sticky=W)
            historial('Ingreso de fecha incorrecto')
        elif valor == 2:
            error_correo = Label(self.master)
            error_correo.config(text='name@domain.com', fg='red')
            error_correo.grid(row = 5, column = 2, padx=2, pady=2, sticky=W)
            historial('Ingreso de correo incorrecto')
    
    def control(self):
        """la función control se encarga de verificar el ingreso y el formato de los datos ingresados antes de conectarse con la base de datos"""
        if self.nombre.get() == '' or self.raza.get() == '' or self.rango.get() =='' or self.fecha.get() == '' or self.correo.get() == '':
            showwarning("Error",'Completar los campos vacíos')
        else:
            oficial = Persona(self.nombre.get(), self.raza.get(), self.fecha.get(), self.rango.get(), self.correo.get())
            nacimiento = oficial.validación_fecha()
            if nacimiento == 1:
                showerror('Error','Wrong date format')
                self.advertencia(nacimiento)
            else:
                email = oficial.validación_mail()
                if email == 2:
                    showerror('Error','Wrong email format')
                    self.advertencia(email)
                else:
                    dato = oficial.cargadatos()
                    insertar(dato)
                    historial('Alta del oficial {0} exitosa'.format(dato[0]))

    def help(self):
        showinfo("La Historia", '''La Flota Estelar es la agencia diplomática, científica y defensiva de la Federación Unida de Planetas. Creada en 2161 con la firma de los Artículos de la Federación, su principal objetivo es adquirir conocimiento del universo, defender la integridad de la Federación y sus miembros y promover la paz y cooperación interestelar. El Comando de la Flota es la autoridad operativa de la Flota Estelar.''')





