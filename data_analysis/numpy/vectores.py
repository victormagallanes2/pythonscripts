import numpy as np


vector1 = np.array([1, 2, 3, 5, 9, 2])
miArray = np.arange(10)


print(miArray.ndim) # Consultamos el número de dimensiones
print(miArray.shape)   # Consultamos cuantas unidades existen
print(miArray.size)   # Consultamos cuantas unidades existen
print(miArray.dtype)   # Consultamos el tipo de elementos del array
print(miArray.itemsize)   # tamaño en bytes
print(miArray.data)   # Consultamos el buffer de memoria.

print(vector1.shape)
print(vector1.size)

print("- sumarle 1 a cada elemento del vector:")
print(vector1+1)
print("- multiplicar por 5 cada elemento del vector:")
print(vector1*5)

print("- suma de los elementos:")
print(np.sum(vector1))

print("- promedio (media) de los elementos:")
print(np.mean(vector1))