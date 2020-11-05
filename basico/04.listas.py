"""Las listas son un tipo de dato en el que se pueden almacenar
   otros datos, inclusive funciones"""

lista = [1, "loquesea", 5.5, 4, [6, 8, "celular"]]
print(lista)
# imprime en consola:
# [1, 'loquesea', 5.5, 4, [6, 8, 'celular']]


"""A cada item de la lista se le asigna un valor, comenzando desde 0
  con esto podemos seleccionar el valor de la lista que queramos"""
print(lista[0])
# imprime en consola:
# 1


# Tambien podemos reescribir el valor de una lista ubicandolo por su posicion
lista[0] = "juan"
print(lista)
# imprime en consola:
# ['juan', 'loquesea', 5.5, 4, [6, 8, 'celular']]


# Con la funcion append es posible asignar mas elementos al final de la lista
lista.append(9)
print(lista)
# imprime en consola:
# ['juan', 'loquesea', 5.5, 4, [6, 8, 'celular'], 9]


# Con la funcion insert es posible insertar elementos asignandole una posicion
lista.insert(3, "jose")
print(lista)
# ['juan', 'loquesea', 5.5, 'jose', 4, [6, 8, 'celular'], 9]


# Con la funcion pop es posible eliminar un elemento de la lista en una posicion dada
lista.pop(1)
print(lista)
# imprime en consola:
# ['juan', 5.5, 'jose', 4, [6, 8, 'celular'], 9]


vowels = ['e', 'a', 'u', 'o', 'i']
# Con la funcion sort es posible ordenar los elementos de una lista
vowels.sort()
print('Sorted list:', vowels)
# imprime en consola:
# Sorted list: ['a', 'e', 'i', 'o', 'u']

# Tambien es posible cambiar el orden de la lista al inverso
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('Sorted list (in Descending):', vowels)
# imprime en consola:
# Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']




