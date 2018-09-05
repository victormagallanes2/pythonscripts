import sys

numero1 = sys.argv[1] #segundo argumento en la linea de comandos
numero2 = sys.argv[2] #tercer argumento en la linea de comandos

try:
 total = float(numero1) + float(numero2)
 print("La suma total de", numero1, "y", numero2, "es igual a", total)
except ValueError:
 print("Los argumentos para sumar deben de ser en formato numerico")