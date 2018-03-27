class PruebaAtributos(object):
    def __init__(self):
        self.publico = "atributo publico"
        self.__privado = "atributo privado"
    
''' objec = PruebaAtributos()
print(objec.publico)
print(objec.__privado) ''' # nos dara error porque es privado


class Pruebafunciones(object):
    def metodo_publico(self):
        print("Soy publico")

    def __metodo_privado(self):
        print("Soy privado")

    def get_privado(self): # para acceder a la funcion privada
        return self.__metodo_privado()

    def set_privado(self, valor): # para modificar a la funcion privada
        self.__metodo_privado() = valor

objec = Pruebafunciones()
objec.metodo_publico()
''' objec.__metodo_privado() ''' # Da error
objec.get_privado()
objec.set_privado("nuevo valor")      