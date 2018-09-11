import os
import zipfile
from zipfile import ZipFile


""" zipfile te permite:
    - comprimir y descomprimir archivos y directorios """


class Zipfile(object):
    def zip_file(self):
        with ZipFile('comprimido.zip', 'w') as nuevozip:
            nuevozip.write('../resources/archivo.txt')
        pass

    def zip_folder(self, path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
        pass
        


ziph = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
Objeto = Zipfile()
Objeto.zip_folder('tmp/', ziph)
