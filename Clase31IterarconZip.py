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