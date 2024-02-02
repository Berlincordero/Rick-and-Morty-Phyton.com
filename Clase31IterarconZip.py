'''
Iterar con zip en Python
La función zip() de Python viene incluida por defecto 
en el namespace, lo que significa que puede ser usada
sin tener que importarse.

Dicho de otra manera, si pasamos dos listas a zip como entrada,
el resultado será una tupla donde cada elemento tendrá 
todos y cada uno de los elementos i-ésimos de las pasadas
como entrada.
'''
'''
Veamos un ejemplo. Como podemos ver, el resultado
tras aplicar zip es una lista con a[0]b[0] en el primer
elemento y a[1]b[1] como segundo.
'''
a = [1, 2] # tenemos elementos dentro de las llaves en posicion a y b
b = ["Uno", "Dos"] # igual tenemos en la misma posiciones elementos en la variable b
c = zip(a, b) # por lo tanto la funcion que vamos a imprimir nos va listar y unirn a con a y b con b de respectivas variables

print(list(c)) # por lo tanto imprimira la variable c que contiene la accion del zip con los elementos a y b
# [(1, 'Uno'), (2, 'Dos')]  como vemos los agrupara respectivamente a con a y b con b

'''
Puede parecer una función no muy relevante,
pero es realmente útil combinada con un for
para iterar dos listas en paralelo.
'''
#Veamos

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a,b)

for numero, texto in zip(a, b):
    print("Numero", numero, "letra", texto)
    
# Número 1 Letra Uno
# Número 2 Letra Dos

#Zip() con n argumentos
'''
Como cabría esperar, dado que zip está definido para 
un número arbitrario de parámetros de entrada, es posible 
también posible usar un único valor. 
El resultado son tuplas de un elemento.

'''
numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))


# Salida: [(1,), (2,), (3,), (4,), (5,)]

#Zip() con diccionarios
'''
Hasta ahora nos hemos limitado a usar zip con listas,
pero la función está definida para cualquier clase iterable.
Por lo tanto podemos usarla también con diccionarios.

Si realizamos lo siguiente, a,b 
toman los valores de las key del diccionario. 
Tal vez algo no demasiado interesante.
'''
esp = {'1': 'Uno', '2': 'Dos', '3': 'tres'}
eng = {'1': 'One', '2': 'Two', '3': 'three'}

for a, b in zip(esp, eng):
    print(a, b)

#Salida:

# 1 1
# 2 2
# 3 3

'''
Sin embargo, si hacemos uso de la función items, 
podemos acceder al key y value de cada elemento.
'''
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three

#NOTA: Nótese que en este caso ambas key k1 y k2 son iguales.


#Deshacer el zip()
'''
Con un pequeño truco, es posible deshacer el zip 
en una sola línea de código. Supongamos que hemos 
usado zip para obtener c.
'''
a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c)) #aqui se podria leer de la siguiente forma imprima la lista con los elementos de (c)
# [(1, 'One'), (2, 'Two'), (3, 'Three')]

# ¿Es posible obtener a y b desde c? Sí, tan sencillo como:

c = [(1, 'One'), (2, 'Two'), (3,'Three')]
a, b = zip(*c)

print(a) # (1, 2, 3)
print(b) # ('One', 'Two', 'Three')

#NOTA: Nótese el uso de *c, lo que es conocido como unpacking en Python.