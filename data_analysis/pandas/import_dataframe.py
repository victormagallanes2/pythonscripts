import pandas as pd

# importar data de un csv
# doc = pd.read_csv('../../resources/transacciones.csv')
# df = pd.DataFrame(doc)
# print(df)

# importar data de un xlsx, depende de xlrd por lo tanto
# debe instalarla
doc = pd.read_excel('../../resources/transacciones.xlsx')
df = pd.DataFrame(doc)
# la funcion info muestra como vienen los datos
#print(df.info())
# la funcion head muestra el encabezado de las columnas
#print(df.head())

diccionario = { "verduras": ["zanaoria", "remolacha", "tomate"],
                "frutas": ["manzana", "pera", "cambur"]}

df2 = pd.DataFrame(diccionario)
print(df2)