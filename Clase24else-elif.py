#################################################################################################################3
#####Varias Condiciones########################################################################################################
##########################################################################################################################################
'''
Hasta ahora hemos visto como ejecutar un bloque de código
si se cumple una instrucción, u otro si no se cumple,
pero no es suficiente. En muchos casos, podemos tener varias
condiciones diferentes y para cada una queremos un código 
distinto. Es aquí donde entra en juego el elif.
'''
c = 7 # se declara la variable y el valor
if c == 7: # si c es igual e igual a 7
    print("el numero es 7") # imrprima el nuemro es 7
elif c == 8: # o si c es igual e igual a 8
    print("el numero es 8") # imprima el numero es 8 
elif c == 9: # o si c es igual e igual a 9
    print("el numero es 9") # imprima el numero es 9
elif c == 10: # o si c es igual e igual a 10 
    print("el numero es 10") # imprima el numero es 10

# tambien como podemos ver el codigo se jecuta el la primera condicion ya que cumple lo que esta solicitando
    
'''
Con la cláusula elif podemos ejecutar tantos bloques de código 
distintos como queramos según la condición. Traducido al lenguaje natural,
sería algo así como decir: si es igual a 5 haz esto, si es igual a 6 haz lo otro,
si es igual a 7 haz lo otro.
'''

b = 5
if b == 7:
     print("es 7")
elif b == 8:
    print("es 8")
elif b == 9:
    print("es 9")
elif b == 10: 
    print("es 10")
else: 
    print("es otro")

# como vemos al no cumplir ninguna de las condiciones se ejecuta el ultimo bloque donde se indica esto.

'''
Si vienes de otros lenguajes de programación, sabrás que el switch es una forma
alternativa de elif, sin embargo en Python esta cláusula no existe.
'''