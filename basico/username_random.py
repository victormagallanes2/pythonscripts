import random

email = "victormagallanes2@gmail.com"

x = email.split("@")
y = random.randrange(0, 99999, 4)

print(str(x[0])+str(y))


