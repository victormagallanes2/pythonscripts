import math

# Funciones Aritméticas

def getsin(x):

    multiplier = 1
    result = 0
    
  for i in range(1,20,2):
		result += multiplier*pow(x,i)/math.factorial(i)
		multiplier *= -1
		
	return result

getsin(math.pi/2) # returns 1.0
getsin(math.pi/4) # returns 0.7071067811865475


math.ceil(1.001)    # returns 2
math.floor(1.001)   # returns 1
math.factorial(10)  # returns 3628800
math.gcd(10,125)    # returns 5
 
math.trunc(1.001)   # returns 1
math.trunc(1.999)   # returns 1

# Funciones Trigonométricas

math.sin(math.pi/4)    # returns 0.7071067811865476
math.cos(math.pi)      # returns -1.0
math.tan(math.pi/6)    # returns 0.5773502691896257
math.hypot(12,5)       # returns 13.0
 
math.atan(0.5773502691896257) # returns 0.5235987755982988
math.asin(0.7071067811865476) # returns 0.7853981633974484

# Funciones Exponenciales y Logaritmicas

math.exp(5)                      # returns 148.4131591025766
math.e**5                        # returns 148.4131591025765
 
math.log(148.41315910257657)     # returns 5.0
math.log(148.41315910257657, 2)  # returns 7.213475204444817
math.log(148.41315910257657, 10) # returns 2.171472409516258
 
math.log(1.0000025)              # returns 2.4999968749105643e-06
math.log1p(0.0000025)            # returns 2.4999968750052084e-06
 
math.pow(12.5, 2.8)              # returns 1178.5500657314767
math.pow(144, 0.5)               # returns 12.0
math.sqrt(144)                   # returns 12.0
