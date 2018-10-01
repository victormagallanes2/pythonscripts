import pandas as pd
import numpy as np


doc = pd.read_csv('../../resources/transacciones.csv')
df = pd.DataFrame(doc)
#print(df)

# suma resta multiplicacion y division de columnas
operaciones = df['debit'] + df['credit'] - df['Move_id/id'] * df['credit'] / df['credit']

print(operaciones)

