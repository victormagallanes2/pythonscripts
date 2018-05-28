import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


doc = pd.read_csv('Mesas_Estados.csv')
df = pd.DataFrame(doc)

estados = df['ESTADOS']
votantes = df['VOTANTES']

eje_x = np.arange(len(estados))
plt.bar(eje_x, votantes, align='center', alpha=0.5)
plt.xticks(eje_x, estados, rotation=90)
plt.ylabel('votantes')
plt.title('Votantes por estados') 
plt.savefig('votantes.png')
plt.show()
