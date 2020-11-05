#Usando el operador Filter
nums = [0, 2, 5, 8, 10, 23, 31, 35, 36, 47, 50, 77, 93]
result = filter(lambda x: x % 2 == 0, nums)
print(result)