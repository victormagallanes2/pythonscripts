import crypt

x = "loquesea"
password = crypt.crypt(x, "salt")
print(password)
