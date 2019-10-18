def funcion_decoradora(funcion_a_decorar):
    def funcion_de_retorno():
        print("resultado")
        funcion_a_decorar()
    return funcion_de_retorno

@funcion_decoradora
def suma():
    print(2+2)

@funcion_decoradora
def resta():
    print(8-2)


suma()
resta()