from peewee import *
  
try:
    db = SqliteDatabase('oficiales.db')
 
    class BaseModel(Model):
        class Meta:
            database = db
 
    class Oficial(BaseModel):
        nombre = CharField(unique = True)
        raza  = CharField()
        fecha = CharField()
        rango = CharField()
        correo = CharField()
        sector = CharField()
        foto = CharField(null= True)

        def __str__(self,):
            return 'Sector: {0}'.format(self.sector)
 
    db.connect()
    db.create_tables([Oficial])
 
except:
    print("Problema de conexión")
