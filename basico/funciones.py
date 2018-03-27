a = 3
b = 8
c = 2

lista = [1, 2, 3, 4]

def suma(f, r):
	z = f + r
	return z

def resta(f, r):
	return f - r

def suma_variante(a= 2, b= 8):
	g = a + b
	return g

def multiplicacion(s, k):
	return s * k
	

print suma(2, 2)
print resta(b, c)
print suma_variante()
s = suma(2, 2)
k = resta(b, c)
print multiplicacion(s, k)