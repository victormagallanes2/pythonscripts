# -*- coding: utf-8 -*-

diccionario = {"verdura1": "zanaoria",
	       "verdura2": "remolacha",
	       "verdura3": "tomate"
	       }

# agrerar items

diccionario["verdura4"] = "apio"
diccionario["verdura5"] = [1, 2, 3]
# modificar

diccionario["verdura3"] = "papa"

# eliminar

del diccionario["verdura2"]

# lee

f = diccionario.keys()
print f

g = diccionario.values()
print g

for x in diccionario:
	print x

for x in diccionario:
	print diccionario[x]


for x, y in diccionario.items():
	print x, ":", y


import json

with open('json_anidado.json', 'r') as file:
    data = json.load(file)
    
    s = [x.get('_source') for x in data["hits"]["hits"]]
    print s



