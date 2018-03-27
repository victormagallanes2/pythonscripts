def argumentos_lista(*args):
    # args es una tupla
    print(args)
    for x in args:
        print(x)


def argumentos_diccionario(**kwargs):
    # kwargs es una diccionario
    print(kwargs)
    for x in kwargs.items():
        print(x)


def argumentos_mesclados(*args, **kwargs):
    for x in args:
        print(x)
    for y in kwargs.items():
        print(y)


argumentos_lista(1, 2, 6, 2, "texto")
argumentos_diccionario(color="rojo", numero=10)
argumentos_mesclados(1, 2, 6, 2, "texto", color="rojo", numero=10)
