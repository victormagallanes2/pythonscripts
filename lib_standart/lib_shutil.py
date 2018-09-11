
from os import path
import shutil

""" shutil te permite:
    - copiar, mover, eliminar y renombrar
      archivos y carpetas
    - comprobar si un objeto existe"""

class Shutil():
    def CopyArchive(self):
        if(path.exists("../resources/archivo.txt")):
            rutanombre = path.realpath('../resources/archivo.txt')
            archivoNuevo = rutanombre + '.bak'
            shutil.copy(rutanombre, archivoNuevo)
        else:
            print("No existe archivo")
        pass


Objeto = Shutil()
Objeto.CopyArchive()
