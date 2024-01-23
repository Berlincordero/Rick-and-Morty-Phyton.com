'''
Introducción al continue
El uso de continue al igual que el ya visto break,
nos permite modificar el comportamiento de 
los bucles while y for.

Concretamente, continue se salta todo el código restante
en la iteración actual y vuelve al principio en el caso 
de que aún queden iteraciones por completar.

La diferencia entre el break y
continue es que el continue no rompe el bucle,
si no que pasa a la siguiente iteración saltando el código 
pendiente.

En el siguiente ejemplo vemos como al encontrar la letra P
se llama al continue, lo que hace que se salte el print().
Es por ello por lo que no vemos la letra P impresa en pantalla.

'''
cadena = "Python"
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
    
# Salida:
# y
# t
# h
# o
# n

'''
El continue salta hasta el final del bloque, 
dejando sin ejecutar lo restante, pero continúa en la siguiente iteración.
'''

for i in range(3):
    if i == 1:     #como observamos el continue es para que se salte a
        continue   # la ultima accion que en dicho caso imprimi la accion condicional
    print(i) 
    
    #Transcripcion 
    '''
    para i en rango de 3 
    si i es igual a 1 
    continue e imorima i 
    que este caso imprimira el rango de alcance exceptuando el 3 mismo 
    que seria lo que esta dentro de este rango
    '''
#################################################################################################################################################
'''
En el siguiente ejemplo podemos ver como cuando 
la x vale 3, se llama al continue, lo que hace que se
salte el resto de código de la iteración (el print()).
Por ello, vemos como el número 3 no se imprime en pantalla.
'''
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#Salida: 4, 2, 1, 0

# otras palabras el continue es perfecto para saltarse un elemento
