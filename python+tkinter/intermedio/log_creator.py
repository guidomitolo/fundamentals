from datetime import *

"""módulo para registrar eventos en archivo externo (txt)"""

def historial(arg):
    now = datetime.now()
    timestamp = now.strftime(" %d/%m/%Y %H:%M:%S\n")
    archivo = open('log_starfleet.txt', 'a')
    archivo.write(arg)
    archivo.write(timestamp)
    archivo.close()