import re

patron = re.compile(r'\bfoo\b')  # busca la palabra foo


# texto de entrada# texto 
texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""

# match nos devuelve None porque no hubo coincidencia al
#comienzo del texto
print(patron.match(texto))
# match encuentra una coindencia en el comienzo del texto
m = patron.match('foo bar')
print(m)
# search nos devuelve la coincidencia en cualquier ubicacion.
s = patron.search(texto)
print(s)
# findall nos devuelve una lista con todas las coincidencias
fa = patron.findall(texto)
print(fa)
# finditer nos devuelve un iterador
fi = patron.finditer(texto)
print(fi)

meses = 'ene+feb+mar+abr+may+jun'

patro = re.compile('\+')
print(patro.split(meses))  
# ['ene', 'feb', 'mar', 'abr', 'may', 'jun']

patron = re.compile('\+')
print(patro.split(meses, maxsplit=1))  
# ['ene', 'feb+mar+abr+may+jun']