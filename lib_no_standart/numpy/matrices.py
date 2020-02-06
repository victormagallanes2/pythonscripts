#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


# 1 Dimencion
vector1 = np.array([1, 2, 3])

# 2 Dimenciones
matriz = np.array([[2, 3, 4], [4, 1, 5], [5, 2, 3]])


lista_de_listas = [[1, -4], [12, 3], [7, 5.0]]

a = np.array(lista_de_listas)

print("- Matriz original:")
print(a)

print("- Le asignamos el valor 4 a los elementos de la columna 0:")
a[:, 0] = 4
print(a)


print("- Dividimos por 3 la columna 1:")
a[:, 1] = a[:, 1] / 3.0
print(a)

print("- Multiplicamos por 5 la fila 1:")
a[1, :] = a[1, :] * 5
print(a)

print("- Le sumamos 1 a toda la matriz:")
a = a + 1
print(a)


# 3 Dimenciones
matriz3D = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
