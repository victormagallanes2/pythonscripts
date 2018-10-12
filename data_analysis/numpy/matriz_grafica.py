#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Creamos la figura
fig = plt.figure()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111, projection='3d')

# Datos en array bi-dimensional
x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
y = np.array([[5, 6, 7, 8, 2, 5, 6, 3, 7, 2]])
z = np.array([[1, 2, 6, 3, 2, 7, 3, 3, 7, 2]])

j = x * y

# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.plot_wireframe(x, y, j)

# Mostramos el gráfico
plt.show()
