from zipfile import ZipFile


class Comprimir():
    def Zip(self):
        with ZipFile('comprimido.zip', 'w') as nuevozip:
            nuevozip.write('archivo.txt')
        pass


Objeto = Comprimir()
Objeto.Zip()
