lista = [1, "loquesea", 5.5, 4, [6, 8, "celular"]]

lista[0] = "juan"
lista.append(9)
lista.insert(0, "jose")
lista.pop(1)
print(lista)


# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)



planets = [
    ("jupiter", 5612, 0.26, 65),
    ("mercury", 600, 12, 84),
    ("eart", 800, 120, 20)
    ]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)



