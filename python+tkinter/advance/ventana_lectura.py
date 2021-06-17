from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from PIL import Image, ImageTk
from conexion import *
from intro import *
import ventana_carga as vc
import ventana_modificar as vm
import random

class Lectura(welcome):

    """clase que da forma a la primer y más relevante pantalla de la app, la cual permite visualizar la base 
    y da acceso a otras funciones"""

    def __init__(self,parent):

        self.welcome = parent
        self.inside=Toplevel(self.welcome)
        self.inside.title("Sector Crew")

        self.titulo = Label(self.inside, text="Officer's Database", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)
 
        self.tree = ttk.Treeview(self.inside, height = 10, columns = 7)
        self.tree["columns"]=("Nombre","Raza","Fecha", "Rango", "Correo", "Sector")
        self.tree.grid(row = 1, column = 0, columnspan = 6)
        self.tree.column("#0", width=40, minwidth=15)
        self.tree.heading("#0",text="ID",anchor=CENTER)
        self.tree.heading("Nombre", text = 'Nombre', anchor = CENTER)
        self.tree.column("Raza", width=150, minwidth=15)
        self.tree.heading("Raza", text = 'Raza', anchor = CENTER)
        self.tree.heading("Fecha", text = 'Fecha de Nacimiento', anchor = CENTER)
        self.tree.column("Rango", width=150, minwidth=15)
        self.tree.heading("Rango", text = 'Rango', anchor = CENTER)
        self.tree.heading("Correo", text = 'Correo', anchor = CENTER)
        self.tree.heading("Sector", text = 'Jurisdicción', anchor = CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.pick) # asociación click del mouse + función "self.pick"
        self.selected = []
        
    def pantalla(self,):
        """ función que inserta la base de datos en el treeview (para actualizar la tabla primero se borra lo cargado antes de la última modificación)"""
        oficiales = self.tree.get_children()
        for oficial in oficiales:
            self.tree.delete(oficial)
        for individuo in Oficial.select():
            self.tree.insert('', 0, text = individuo.id, values = (individuo.nombre, individuo.raza, individuo.fecha, individuo.rango, individuo.correo, individuo))

        # los comandos de los botones de carga y modificación pasan el TopLevel (para agregar etiquetas) y el self/objeto de la clase Lectura (para ejecutar un método)
        Button(self.inside, text='Cargar',command=lambda:vc.Carga(self.inside,self)).grid(row=11, column=2)
        Button(self.inside, text='Modificar',command=lambda:vm.Modificar(self.inside,self)).grid(row=11, column=4)
        
        Button(self.inside, text='Ver Foto',command=self.visualizar).grid(row=11, column=3)    
        Button(self.inside, text='Eliminar',command=self.delete).grid(row=11, column=5)
        
        menubar = Menu(self.inside)
        menuFile = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=menuFile)
        menuFile.add_command(label="Estilo", command=self.estilo)
        menuFile.add_command(label="Exit",command=lambda:self.inside.destroy())
        self.inside.config(menu=menubar)
        
        self.inside.grab_set()
        self.inside.focus_set()
        self.inside.wait_window()
    
    def estilo(self,):
        """función que permite cambiar el fondo de la app"""
        colors = ['gainsboro', 'linen','indian red', 'saddle brown', 'blue']
        clave = random.choice(colors)
        self.inside.config(bg=clave)
        self.titulo.config(bg=clave)
        self.realizar()
    
    def pick(self,evento):
        """la función registra el evento en el atributo self.selected"""
        self.selected = evento.widget.selection()
    
    def delete(self,):
        """función que descompone la data almacenada en "self.selected" para poder ejecutar la acción de borrar el registro (con el consentimiento del humano)"""
        if type(self.selected) == list:
            showinfo('Suprimir', 'Primero seleccione un oficial')
        else:
            if askyesno('Suprimir','¿Está seguro que desea suprimir el registro?'):
                for dato in self.selected:
                    ver = (self.tree.item(dato)['values'])
                erase(ver[0],self)
            else:
                pass
    
    def visualizar(self,):
        """función que permite ver las imagenes de las rutas cargadas en la base de datos"""
        if type(self.selected) == list:
            showinfo('Ver ID', 'Primero seleccione un oficial')
        else:
            for dato in self.selected:
                ver = (self.tree.item(dato)['values'])
                imgpath = Oficial.select().where(Oficial.nombre == ver[0]).get().foto
                try:
                    abrir = Image.open(imgpath)
                    foto_carnet = Toplevel(self.inside)
                    cuadro = Frame(foto_carnet, borderwidth=1)
                    cuadro.pack(fill="both", expand=YES, side=TOP)
                    render = ImageTk.PhotoImage(abrir)
                    img = Label(cuadro, image=render)
                    img.image = render
                    img.pack(fill="both", expand=YES, side=TOP)
                    Button(foto_carnet, text='Cerrar', command=lambda:foto_carnet.destroy()).pack(anchor=CENTER, side=BOTTOM, pady=10)
                except AttributeError:
                    showinfo('Ver ID','No se ha guardado una imagen')
            else:
                pass