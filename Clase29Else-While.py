'''
Else y while
Algo no muy corriente en otros lenguajes de programación
pero si en Python, es el uso de la cláusula else al final 
del while. Podemos ver el ejemplo anterior mezclado con el 
else. La sección de código que se encuentra dentro del else,
se ejecutará cuando el bucle termine, pero solo si lo hace 
“por razones naturales”. Es decir, si el bucle termina 
porque la condición se deja de cumplir, y no porque se ha 
hecho uso del break.
'''
x = 10
while x > 10:
    x -= 1
    print(x)
else:
    print("El bucle ha finalizado")
    
# Ejemplo 2

x = 25

while x != 25:
    x += 1
    print(x)
else:
    print("la operacion se completo")

z = 50

while z != 50:
    z -= 1
    print(x)
else:
    print("error")
    
'''
Podemos ver como si el bucle termina por el break,
el print() no se ejecutará. Por lo tanto, se podría 
decir que si no hay realmente ninguna sentencia break
dentro del bucle, tal vez no tenga mucho sentido el
uso del else, ya que un bloque de código fuera del 
bucle cumplirá con la misma funcionalidad.
'''

x = 15 

while True:
    x -= 1 
    print(x)
    if x == 0:
        break # aqui se detendra la accion tal como lo vimos en la clase del break 
else:
    # como vemos el print no se ejecutara de hecho el color de linea lo delata un poco 
    print("Fin del bloque")

# como vemos solo imprimira la primera condicion la segunda que contiene el break no se ejecuta 
