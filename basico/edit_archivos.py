class Archivos():
    def Write():
        archivo = open('archivo.txt', 'w+')
        archivo.write("Se escribio")
        pass
        """La funcion open es para crear y recibe dos parametros,
           el nombre del archivo y la accion a ejecutar
           la letra w significa el modo de acceso escribir
           el simbolo + significa: si no esta creado
           que se cree El metodo write es el que escribe"""

    def WriteUltimateLine():
        archivo = open('archivo.txt', 'a+')
        archivo.write("\nOtra liena")
        archivo.close()
        pass
        """letra a significa escribir despues de
        la ultima linea del archivo"""

    def ReadLinea():
        archivo = open('archivo.txt', 'r')
        if archivo.mode == 'r':
            lineaArchivo = archivo.readlines()
            for x in lineaArchivo:
                print x
        archivo.close()
        pass
