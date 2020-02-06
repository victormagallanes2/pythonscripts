a = 3
b = 8
c = 2

def suma(f, r):
	z = f + r
	return print(z)


def resta(f, r):
	return print(f - r)


def multiplicacion(s, k):
	return print(s * k)


lista = [suma(a,b), resta(a,b), multiplicacion(a,b)]

while (len(lista) > 0):
    lista.pop(0)

