#Usando el operado filter
from functools import reduce #en python3 reduce se encuentra en modulo functools

nums = [47,11,42,13]
result = reduce(lambda x, y: x + y, nums)
print(result)
