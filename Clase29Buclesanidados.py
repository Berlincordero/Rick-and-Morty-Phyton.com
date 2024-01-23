'''
Bucles anidados
Ya hemos visto que los bucles while tienen una condición
a evaluar y un bloque de código a ejecutar.
Hemos visto ejemplos donde el bloque de código son 
operaciones sencillas como la resta -, pero podemos 
complicar un poco mas las cosas y meter otro bucle while 
dentro del primero. Es algo que resulta especialmente útil 
si por ejemplo queremos generar permutaciones de números, 
es decir, si queremos generar todas las combinaciones posibles. 
Imaginemos que queremos generar todas las combinaciones
de de dos números hasta 2. Es decir, 0-0, 0-1, 0-2,… 
hasta 2-2.

'''
# Permutaciones a generar

i = 0
j = 0
while i < 3:
    while j < 3:
       print(i,j)
       j += 1 
    i += 2
    j = 0
# Salida
# 0 0
# 0 1
# 0 2
# 2 0
# 2 1
# 2 2
'''
Vamos a analizara el ejemplo paso por paso. 
El primer bucle genera números del 0 al 2, lo que corresponde
a la variable i. Por otro lado el segundo bucle genera
también número del 0 al 2, almacenados en la variable j.
Al tener un bucle dentro de otro, lo que pasa es que por
cada i se generan 3 j. Muy importante no olvidar que al 
finalizar el bucle de la j, debemos resetear j=0 para que 
en la siguiente iteración la condición de entrada se cumpla.
'''

# Ejemplo 2
a = 1
b = 2 
while a < 6:
    while b < 8:
        print(a,b)
        a += 2
        b += 5
        a = 0 

'''
Podemos complicar las cosas aún más y tener tres bucles 
anidados, generando combinaciones de 3 elementos
con número 0, 1, 2. En este caso tendremos
desde 0,0,0 hasta 2,2,2.
'''
i, j, k, l, m = 0, 0, 0, 0, 0
while i < 5:
    while j < 5:
        while k < 5:
            while l < 5:
                while m < 5:
                    print(i,j,k,l,m)
                    k += 1 
                    j += 1
                    l += 1
                    k = 0
                    i += 1
                    j = 0
                    l += 1
                    m = 0
                    l = 0
                    m += 1
                
                