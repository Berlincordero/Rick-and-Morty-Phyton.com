'''
ahora veremos otro ejemplo de condicional 
usando diferentes variables y asignadoles un valor y con ello 
realizar una operacion usando una variable booleana (logica)
'''
#Definimos una variable x con una cadena(oracion o parrafo) esto seria una variable tipo string
x = "El valor de (a+b)*C es" # Ejemplo de una ecuacion de lado + lado * base
#Ahora hacemos deiferentes asiganciones a nuestras variables para la operacion
a, b, c= 5,7,2
#Realizamos unas operaciones con a,b,c
d = (a+b) *c # d y x seran las variables que nos mostraran el resultado
#Ahora definimos una variable booleana esta variable tecnicamente nos dira cierto o falso y si es correcto en est caso imprimira el resultado
imprimir = True #  esta variable nos permite hacer la condicional

# si imprimir es print() imprimame x y d 
if imprimir: 
    print(x, d)
    #Salida: El valor de (a+b)*C es 24
#un condicional if. Justo después tenemos un print() identado con cuatro espacios. Por lo tanto, todo lo que tenga esa identación pertenecerá al bloque del if.
