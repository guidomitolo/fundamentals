from datetime import *

"""módulo para registrar eventos en archivo externo (txt)"""

def historial(funcion):
    call_reg = 0
    def registro(*args):  
        nonlocal call_reg
        call_reg +=1
        if funcion.__name__ is 'insertar':
            entry = 'Alta del oficial {0} exitosa'.format(args[0][0])
        elif funcion.__name__ is 'erase':
            entry = 'Eliminación del registro correspondiente al oficial {0} exitosa'.format(args[0])
        elif funcion.__name__ is 'update':
            entry = 'Modificación del registro del oficial {0} exitosa'.format(args[0])
        elif funcion.__name__ is 'upload':
            entry = 'Se ha cargado una imagen del oficial {0}'.format(args[0])
        conteo = 'La función %s ha sido utilizada %s veces en la presente sesión\n' % (funcion.__name__,call_reg)
        now = datetime.now()
        timestamp = now.strftime(" %d/%m/%Y %H:%M:%S\n")
        archivo = open('log_starfleet.txt', 'a')
        archivo.write(entry)
        archivo.write(timestamp)
        archivo.write(conteo)
        archivo.close()
        return funcion(*args)
    return registro