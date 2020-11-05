"""Las condicionales se usan para ejecutar una instruccion
   siempre y cuando cumpla con una condicion establecida."""

edad = int(input("Ingrese su edad: "))
# input sirve para ingresar parametros desde la consola

# Comprobar si la edad ingresada por consola es mayor o menor a 18
if edad >=18 and edad <= 40:
	print("es joven")
elif edad > 0 and edad < 18:
	print("es menor de edad")
else:
	print("esta pasado")
# imprime en consola:
# Ingrese su edad: 56
# esta pasado
