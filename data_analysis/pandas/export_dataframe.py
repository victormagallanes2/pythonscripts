import pandas as pd

# import csv
doc = pd.read_csv('../../resources/transacciones.csv')
df = pd.DataFrame(doc)

# operaciones
data_filter_id = df.loc[df['Move_id/id'] == 1]
#quivale a select * from df where Move_id/id==1;
# export data filtrada em xlsx
#data_filter_id.to_excel('../../resources/output_pandas.xlsx')
# export data filtrada em csv
data_filter_id.to_csv('../../resources/output_pandas.csv')

