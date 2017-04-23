
from os import path
import shutil


class Shutil():
    def CopyArchive(self):
        if(path.exists("archivo.txt")):
            rutanombre = path.realpath('archivo.txt')
            archivoNuevo = rutanombre + '.bak'
            # shutil.copy(rutanombre, archivoNuevo)
            # shutil.copy copia simple
            # shutil.copystat copia con metadata
            shutil.copy(rutanombre, archivoNuevo)
        else:
            print "No existe archivo"
        pass


Objeto = Shutil()
Objeto.CopyArchive()
