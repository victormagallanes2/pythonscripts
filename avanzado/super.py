"""La función super nos permite invocar y conservar un método o atributo
 de una clase padre (primaria) desde una clase hija (secundaria) sin 
 tener que nombrarla explícitamente. """

# Herencia simple de clase y atributos en python con super()

class Padre(object): #Creamos la clase Padre
	def __init__(self, ojos, cejas): #Definimos los Atributos
		self.ojos = ojos
		self.cejas = cejas
 
		
class Hijo(Padre): #Creamos clase hija que hereda de Padre
	def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
		Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
		self.cara = cara #Especificamos el nuevo atributo para Hijo
 
		
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)

# El codigo anterior expuesto se puede emplear super

class Padre(object): #Creamos la clase Padre
	def __init__(self, ojos, cejas): #Definimos los Atributos
		self.ojos = ojos
		self.cejas = cejas
 
		
class Hijo(Padre): #Creamos clase hija que hereda de Padre
	def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
		super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
		self.cara = cara #Especificamos el nuevo atributo para Hijo
 
		
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)

# Nota: para los atributos super no funciona con herencia multiple

# Super se puede usar para invocar metodos de la clase padre sin reescribirlo

class Agregarelemento(list): #Creamos una clase Agregarelemento heredando atributos de clase list (clase incorporada)
    def append(self, alumno): #Definimos que el método append (de listas) añadirá el elemento alumno
        print (("Añadido el alumno"), (alumno)) #Imprimimos el resultado del método
        super().append(alumno) #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                                    #del método append para la variable alumno
 
Lista1 = Agregarelemento() #Definimos la clase de nuestra lista llamada "Lista1"
Lista1.append ('Matias') #Añadimos un elemento a la lista como lo haríamos normalmente
print (Lista1) #Imprimimos la lista para corroborar que se añadió el alumno

"""Con super puedes invocar funciones de la clase padre en herencia multiple
   respetando el orden de ejecucion MRO (Method Resolution Order)"""


class Perros(object): #Declaramos la clase principal Perros
    def ladrar (self):
        print ("""GUAAAUU GUAAAUU!""")
        
    def grunir (self):
        print ("""GRRRRRR GRRRRR""")
 
class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""guau guau guau""")
        
    def grunir(self):
        print ("""gññññiii gñññiiii""")
 
class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""GuaUUU GUAAAUUU GuaUUU""")
        
    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")
 
    
class Shepadoodle (Caniche, Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()
 
Tommy = Pastor_Aleman()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
                    #Y  si borramos ambos? Imprimirá el ladrido de Perros!
