import os
from os import path

""" os te permite
    - conocer rutas
    - copiar, mover, eliminar y renombrar
      archivos y carpetas
    - comprobar si un objeto es archivo o directorio """

class Os():
    def SaberExistencia(self):
        print "El archivo existe: %s" % str(path.exists("archivo.txt"))
        pass

    def EsArchivo(self):
        print "El archivo es file: %s" % str(path.isfile("archivo.txt"))
        pass

    def EsDirectorio(self):
        print "El archivo es directorio: %s" % str(path.isdir("archivo.txt"))
        pass

    def Ruta(self):
        print "Ruta del archivo: %s" % str(path.realpath("archivo.txt"))
        pass

    def RutaNombre(self):
        print "Solo ruta del archivo: %s" % str(path.split(path.realpath("archivo.txt"))[0])
        print "Solo nombre del archivo: %s" % str(path.split(path.realpath("archivo.txt"))[1])
        pass

    def RutaNombreVariante(self):
        if(path.exists("archivo.txt")):
            rutanombre = path.realpath('archivo.txt')
            ruta, nombre = path.split(rutanombre)
            print "Solo ruta del archivo: %s" % ruta
            print "Solo nombre del archivo: %s" % nombre
        else:
            print "No existe archivo"
        pass

    def RenombrarArchivo(self):
        os.rename('archivo.txt', 'archivorenombrado.txt')
        pass


Objeto = Os()
Objeto.SaberExistencia()
Objeto.EsArchivo()
Objeto.EsDirectorio()
Objeto.Ruta()
Objeto.RutaNombre()
Objeto.RutaNombreVariante()
# Objeto.RenombrarArchivo()
