Dir
dir([objeto]) Si no le pasamos ningún argumento devuelve la lista de nombres con alcance local. Con un argumento trata de devolver una lista de atributos válidos para ese objeto. Si el objeto es un módulo, la lista contiene los nombres de los atributos del módulo. Si el objeto es un tipo o clase de objeto, la lista contiene los nombres de sus atributos, y de forma recursiva de los atributos de sus bases. De lo contrario, la lista contiene los nombres de los atributos del objeto, los nombres de los atributos de su clase, y de forma recursiva de los atributos de las clases base de su clase. La lista resultante está ordenada alfabéticamente.


Ejemplo:

Cuando abrimos python en la terminal, hacemos dir() y nos devuelve:

['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

con el comando help podemos ver la ayuda sobre
la clase o modulo a consultar

Consultar clase:
help(pow)

Consultar lista de modulos:

help('modules')

Listar funciones de un modulo:
import math
dir(math)

Ayuda sobre funciones de un modulo:

help(math.radius)

