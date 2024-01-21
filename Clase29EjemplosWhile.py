'''
Ejemplos while

Árbol de navidad en Python. 
Imprime un árbol de navidad formado con * haciendo 
uso del while y de la multiplicación de un entero
por una cadena, cuyo resultado en Python es replicar 
la cadena.
'''
#Veamos

z = 7 # z representa la linea horizontal 
x = 1 # x representa la linea vertical

while z > 0: # la z es la que representara (*) que formara el arbol
    print(' ' * z + '*' * x + ' ' * z) # aqui debemos interar los espacio para que (*) tome los espacios adelnte y atras para formar el arbol
    
    x += 2 # debemos colocar el valor de dichas variables para la opercion anterior en esteb caso a x se le sumara dos elementos mas apartir de la segunda linea
    z -= 1 # y z se le restara 1 elemento que representara los espacios de inicio y final asi centrado los elemntos correspondientes

# Ejemplo 2
'''
Aunque esta no sea tal vez la mejor forma de iterar 
una cadena es un buen ejemplo para el uso del while e
introducir el indexado de listas con [], que veremos 
en otros capítulos.
'''
text = "Python"
i = 0
while i < len(text): #recordemos que len se utiliza para indexar o listar elementos o characteres
  print(text[:1 + 1]) # en la impresion o resultado el texto o letras se iterara o saltar al siguiente elemento sumandolo al resultado
  i += 1 # siempre recordemos declarar la operacion

#Ejemplo 3
'''
Sucesión de Fibonacci en Python. En matemáticas, 
la sucesión de fibonacci es una sucesión infinita de números 
naturales, donde el siguiente es calculado sumando los dos 
anteriores
'''
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
    

