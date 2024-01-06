'''
Múltiples líneas
En algunas situaciones se puede dar el caso de que queramos tener una sola instrucción en varias línea de código.
Uno de los motivos principales podría ser que fuera demasiado larga, y de hecho en la especificación PEP8 
se recomienda que las líneas no excedan los 79 caracteres.
'''
#Ejemplo: 
'''
x = 1 + 2 + 3 + 4 +\ 
5 + 6 + 7 + 8 
'''
#Haciendo uso de \ se puede romper el código en varias líneas, 


#print(x) 
#Salida 36

#Ejemplo 2:
'''
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)

print(x)
Salida : 36
'''
#Tambien se puede hacer lo mismo para llamadas a funciones
#El codigo se ve mas ordenado siguiendo esta regla
'''
def funcion(a, b, c):
    return a+b+c
d = funcion (10,
             23,
             3)

print(d)
'''
#Salida 36 

'''
Otra forma de asignar variables simplificando la linea 
y mas elegante es la siguiente 
'''
''''
x = y = z = 10 #aqui se le esta asignando el mismo valor a las 3

print(x) # como solo se le esta asignando el mismo valor a las 3 la salida es:
'''
#Salida: 10

#EJEMPLO 2
'''
a, c= 4,2
x, y, z = 1, 2, 3

d = a+c+x+y+z

print(d)
#Salida: 12
'''
#OTRAS REGLAS DE SYNTAXIS
'''
El nombre no puede empezar por un número
No se permite el uso de guiones -
Tampoco se permite el uso de espacios.
'''