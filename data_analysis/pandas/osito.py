import pandas as pd
import numpy as np


doc = pd.read_csv('prueba.csv')

df = pd.DataFrame(doc)

df.set_index('Operacion', 'Move_id/id', inplace=True)
data_filter = df.loc[df['Move_id/id'] == 1]


suma = data_filter['debit'] + data_filter['credit']

da_cero = suma.loc[suma == 0]
no_da_cero = suma.loc[suma != 0]


print(data_filter)
print(suma)
print(da_cero)
print(no_da_cero)
