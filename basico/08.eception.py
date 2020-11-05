"""Las ecepciones se usan para manejar errores, es decir cuando se sepa
   que podria ocurrir un error se puede personalizar el msj que vera el usuario"""


while True:
    try:
        x = int(input("Por favor ingrese un número: "))
        break
    except ValueError:
        print("Oops! No era válido. Intente nuevamente...")