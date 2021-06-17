from tkinter import *
from tkinter.messagebox import *
import random
import mysql.connector
from delete import *
from conexion import *

header = ['ID', 'Nombre','Raza','Fecha','Rango', 'Correo']

class database():
    """esta clase permite conectarse al servidor mysql y manejar las variables de acceso a la base de datos y a la tabla y de ejecucción de queries"""
    def __init__(self, host, user, passwd, database,table):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.table = table
    
    def __str__(self):
        return 'Host: {0}\nUser: {1}\nPass: {2}\nDatabase: {3}\nTable: {4}'.format(self.host,self.user,self.passwd,self.database,self.table)
    
    def create(self):
        try:
            base = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd)
            link = base.cursor()
            link.execute("CREATE DATABASE {0}".format(self.database))
            base = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
            link = base.cursor()
            link.execute("CREATE TABLE {0} (id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Raza varchar(128) COLLATE utf8_spanish2_ci NOT NULL, Fecha varchar(10) COLLATE utf8_spanish2_ci NOT NULL, Rango VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Correo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)".format(self.table))
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    # antes de dar el alta al registro se verifica que la base y la tabla estén creadas. de no estarlo, se crean.
    # luego se verifica que el nombre de usuario no se repita
    def alta(self, dato):
        try:
            base = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd)
            link = base.cursor()
            link.execute("SHOW DATABASES LIKE '{0}'".format(self.database))
            database = link.fetchall()
            if database == []:
                self.create()
                self.alta(dato)
            else:
                self.check(dato)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    
    # se ingresa un nombre nuevo si y sólo si no está repetido y el campo está vacío
    def check(self, dato):
        base = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        link = base.cursor()
        query = "SELECT Nombre FROM {0} WHERE Nombre = '{1}'".format(self.table,dato[0])
        link.execute(query)
        resultado = link.fetchall()
        if resultado == [] or resultado[0][0] != dato[0]:
            base = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
            link = base.cursor()
            fila = "INSERT INTO high_command(Nombre, Raza, Fecha, Rango, Correo) VALUES (%s, %s, %s, %s, %s)"
            entrada = (dato)
            link.execute(fila, entrada)
            base.commit()
            showwarning("Alta de usuario",'Usted ha ingresado {0} oficial'.format(link.rowcount))
        elif resultado[0][0] == dato[0]:
            showwarning("Error",'El usuario ya ha sido ingresado')

    def delete(self,variable):
        
        mibase=mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
        link = mibase.cursor()
        query = "DELETE FROM {0} WHERE Nombre = '{1}'".format(self.table,variable)
        link.execute(query)
        mibase.commit()        

    def leer(self):
        try:
            mibase=mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
            micursor = mibase.cursor()
            fila = "SELECT * FROM {0}".format(self.table)
            micursor.execute(fila)
            resultado = micursor.fetchall()
            return resultado
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))