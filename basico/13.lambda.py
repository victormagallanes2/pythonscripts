def suma(a, b):
	return(a + b)

#usando lambda

s = lambda a, b: a + b
print(s(5, 2))

planets = [
    ("jupiter", 5612, 0.26, 65),
    ("mercury", 600, 12, 84),
    ("eart", 800, 120, 20)
    ]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)