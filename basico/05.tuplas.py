"""Las listas son un tipo de dato en el que se pueden almacenar
   otros datos, inclusive funciones, pero a diferencia de las listas
   estas no pueden ser modificadas"""

mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print mi_tupla[1]
# Salida: 15

print mi_tupla[1:4]
# Devuelve: (15, 2.8, 'otro dato')
print mi_tupla[3:]
# Devuelve: ('otro dato', 25)
print mi_tupla[:2]
# Devuelve: ('cadena de texto', 15)