class Vehiculos(object):
    def __init__(self, col="red", mod="z", llant=0, puert=0, vel=0):
        self.color = col
        self.modelo = mod
        self.llantas = llant
        self.puertas = puert
        self.velocidades = vel 

    def mostrar(self):
        print("color: ", self.color) 
        print("modelo: ", self.modelo)
        print("llantas: ", self.llantas)
        print("puertas: ", self.puertas)
        print("velocidades: ", self.velocidades)  

       
carro = Vehiculos(col="green")
carro.mostrar()
     