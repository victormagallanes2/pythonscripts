#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 5, 9, 10])
y = np.array([5, 8, 4, 3, 2, 4])

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Datos locos')
plt.show()


