class Vehiculos(object):
    color = "red"
    modelo = "z"
    llantas = 0
    puertas = 0
    velocidades = 5      

    def mostrar(self):
        print("color: ", self.color) 
        print("modelo: ", self.modelo)
        print("llantas: ", self.llantas)
        print("puertas: ", self.puertas)
        print("velocidades: ", self.velocidades)  

       
carro = Vehiculos()
carro.color = "blue"
carro.mostrar()