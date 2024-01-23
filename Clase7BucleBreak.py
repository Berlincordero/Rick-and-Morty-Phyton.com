'''
Por último, el break rompe la ejecución del bucle, saliendo del mismo.
'''
x = 0
while True: # mientras esto sea correcto lo que este dentro del bloque while
    print(x) # imprima x 
    if x == 2:
        break # tecnicamente aqui pide que rompa o pare el codigo cuando x sea igual e igual a 2
    x += 1 # x mas e igua a 1 por lo tanto x es igual a mas uno 
'''
podria transcribirse de esta manera si x es igual a 0
mientras imprima x donde sera igual a 2 rompa donde x es mayor
e igual a 1 por lo tanto va a imprimir del 0 al 2 cumpliendo esta condicion
'''
'''
Introducción al break
La sentencia break nos permite alterar el comportamiento
de los bucles while y for. Concretamente, permite terminar
con la ejecución del bucle.
Esto significa que una vez se encuentra la palabra break,
el bucle se habrá terminado.

Break con bucles for
Veamos como podemos usar el break con bucles for. 
El range(5) generaría 5 iteraciones, donde la i valdría de 0
a 4. Sin embargo, en la primera iteración, terminamos
el bucle prematuramente.

El break hace que nada más empezar el bucle, 
se rompa y se salga sin haber hecho nada.
'''

for i in range(5):
    print(i)
    break
    # No llega

# Salida: 0

'''
Un ejemplo un poco más útil, sería el de buscar una letra
en una palabra. Se itera toda la palabra y en el momento 
en el que se encuentra la letra que buscábamos, 
se rompe el bucle y se sale.

Esto es algo muy útil porque si ya encontramos lo que 
estábamos buscando, no tendría mucho sentido seguir
iterando la lista, ya que desperdiciaríamos recursos.
'''
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

# Salida:
# P
# y
# t
# Se encontró la h
'''
Break con bucles while
El break también nos permite alterar el comportamiento del 
while. Veamos un ejemplo.

La condición while True haría que la sección de código
se ejecutara indefinidamente, pero al hacer uso del break,
el bucle se romperá cuando x valga cero.
'''
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

#4, 3, 2, 1, 0
#Por norma general, y salvo casos muy concretos
#si ves un while True, es probable que haya un break dentro del bucle.

'''
Break y bucles anidados
Como hemos dicho, el uso de break rompe el bucle,
pero sólo aquel en el que está dentro.

Es decir, si tenemos dos bucles anidados, 
el break romperá el bucle anidado, pero no el exterior.
'''
for i in range(0, 4):
    for j in range(0, 4):
        break # Nunca se realiza más de una iteración
    print(i, j) #El break no afecta a este for


# 0 0
# 1 0
# 2 0
# 3 0