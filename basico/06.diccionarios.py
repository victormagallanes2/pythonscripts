"""Los diccionarios son otro tipo de datos parecidas a las listas
   pero con una estructura llave valor al igual que los archivos json"""

diccionario = {"verdura1": "zanaoria",
	       "verdura2": "remolacha",
	       "verdura3": "tomate"
	       }
#print(diccionario)

# salida
# {'verdura1': 'zanaoria', 'verdura2': 'remolacha', 'verdura3': 'tomate'}

# agrerar items a diccionario

diccionario["verdura4"] = "apio"
diccionario["verdura5"] = [1, 2, 3]

#print(diccionario)

# salida
# {'verdura1': 'zanaoria', 'verdura2': 'remolacha', 'verdura3': 'tomate', 'verdura4': 'apio', 'verdura5': [1, 2, 3]}


# modificar valores de items en diccionario

diccionario["verdura3"] = "papa"

#print(diccionario)

# salida
#{'verdura1': 'zanaoria', 'verdura2': 'remolacha', 'verdura3': 'papa', 'verdura4': 'apio', 'verdura5': [1, 2, 3]}


# eliminar

del diccionario["verdura2"]

#print(diccionario)

# salida
# {'verdura1': 'zanaoria', 'verdura3': 'papa', 'verdura4': 'apio', 'verdura5': [1, 2, 3]}


# lee items de un diccionario
# leer llaves

f = diccionario.keys()
#print(f)

# salida
# dict_keys(['verdura1', 'verdura3', 'verdura4', 'verdura5'])

# leer valores
g = diccionario.values()
#print(g)

# salida
# dict_values(['zanaoria', 'papa', 'apio', [1, 2, 3]])

# recorrer diccionario llaves
# for x in diccionario:
# 	print(x)

# salida
# verdura1
# verdura3
# verdura4
# verdura5

# recorrer diccionario valores
# for x in diccionario:
# 	print(diccionario[x])

# salida
# zanaoria
# papa
# apio
# [1, 2, 3]

# recorrer diccionario llaves y valores
# for x, y in diccionario.items():
# 	print(x, ":", y)

# salida
# verdura1 : zanaoria
# verdura3 : papa
# verdura4 : apio
# verdura5 : [1, 2, 3]


# recorrer json complejo
# import json

# with open('../resources/json_anidado.json', 'r') as file:
#     data = json.load(file)
    
#     s = [x.get('_source') for x in data["hits"]["hits"]]
#     print(s)



