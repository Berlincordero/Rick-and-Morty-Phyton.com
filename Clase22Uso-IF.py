'''
Uso del if
Un ejemplo sería si tenemos dos valores a y b que queremos dividir. 
Antes de entrar en el bloque de código que divide a/b, sería importante verificar
que b es distinto de cero, ya que la división por cero no está definida. Es aquí donde entran los condicionales if.

'''
a = 4 # aqui se le asigna el valor de 4 a la variable a
b = 2 # aqui se le asigna el valor de 2 a la variable
if b != 0: # si b es diferente o igual a o entonoces 
    print(a/b) # imprima a divido entre b 
'''
En este ejemplo podemos ver como se puede usar un if en Python. Con el operador != 
se comprueba que el número b sea distinto de cero, y si lo es, se ejecuta el código que está identado. Por lo tanto un if tiene dos partes:

La condición que se tiene que cumplir para que el bloque de código se ejecute, en nuestro caso b!=0.

El bloque de código que se ejecutará si se cumple la condición anterior.

Es muy importante tener en cuenta que la sentencia if debe ir terminada por :
y el bloque de código a ejecutar debe estar identado. Si usas algún editor de código, seguramente la identación se producirá 
automáticamente al presionar enter. Nótese que el bloque de código puede también contener más de una línea, es decir puede contener más de una instrucción.
'''


if b != 0: #Todo lo que vaya después del if y esté identado, será parte del bloque de código que se ejecutará si la condición se cumple. 
    c = a/b
    print("Dentro del if") # Por lo tanto el segundo print() “Fuera if” será ejecutado siempre, ya que está fuera del bloque if.
    print("Fuera del if ")
    
################################################################################################################################################################################################################################################################################################################################

if b > 0: # Existen otros operadores como el de comparar si un número es mayor que otro. Su uso es igual que el anterior.
    print(a/b)


################################################################################################################################################################################################################################################################################################################################

'''
Se puede también combinar varias condiciones entre el if y los :. Por ejemplo, se puede requerir que un número sea mayor que 5 y además menor que 15.
'''
a = 10
if a > 5 and a < 15: 
    print("Mayor que 5 y menos que 15") #Tenemos en realidad tres operadores usados conjuntamente, que serán evaluados por separado hasta devolver el resultado final, que será True si la condición se cumple o False de lo contrario.

################################################################################################################################################################################################################################################################################################################################

#un dato importante en python no se puede dejar un bloque vacio como en otros lenjuages por que dara sintaxis Error.
#Ejemplo:

#  if a > 5:

#si estamos desarrollando alguna otra tarea es necesarop usar el pass para que se salte dicha funcion

if a >5:
    pass # esta accion hace que salte dicha funcion para continuar con el siguiente bloque de codigo 

#Realmente pass no hace nada, simplemente es para tener contento al interprete de código.

##################################################################################################################################################################################################################################################################################################################################

# Algo no muy recomendable pero si es util si es bloque o linea de codigo es pequeña
# es posible, es poner todo el bloque que va dentro del if en la misma línea, justo a continuación de los :

if a > 5: print("Es > 5") # see lee sencillo en una sola linea (si a es mayor que 5 entonces imprima es mayor que 5)

# tambien si el  código tiene más de una línea, se pueden poner también en la misma línea separándolas con ;.

if a > 5: print("Es > 5") ; print("dentro del if") # se coloca en la misma linea usando (;)















