#!usr/bin/python
# -*- coding: utf-8 -*-

# Nota esta forma de usar super solo fuciona en python3

class Persona(object):
	def __init__(self, nombre, direccion):
		self.nombre = nombre
		self.direccion = direccion

	def function1(self):
		print(self.nombre +" "+ self.direccion)

class Empleado(Persona):
    def __init__(self, sueldo, cargo, nombre_empleado, direccion_empleado):
        super().__init__(nombre_empleado, direccion_empleado)
        self.sueldo = sueldo
        self.cargo = cargo
        pass

    def function2(self):
        super().function1()
        print (self.sueldo, self.cargo)
		



obj2 = Empleado("tomas", "sucasa", "100000","programmer")
print(obj2.function2())
		
		