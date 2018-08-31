import math

def area(r):
    return math.pi * (r**2)

areas = []
redii = [ 2, 4, 6, 8]

for r in redii:
    a = area(r)
    areas.append(a)

#print(areas)

# x = list(map(area, redii))
# print(x)

# usando lambda

y = list(map(lambda r: math.pi * (r**2), redii))
print(y)