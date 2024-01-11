'''
Funciones: def, return, lambda, pass, yield
Todas ellas relacionadas con las funciones.
'''

#DEF
#El uso de def nos permite crear una función.

def funcion_suma (a, b): # aqui estamos diciendo que la funcion es tipo suma y con los valores a y b 
    print ("la suma es", a + b) # aqui que nos imprima el resultado de dicha funcion
    
funcion_suma(3 , 5)  # aqui le asignamos los valores 3 y 5 a la funcion suma
# por lo tanto se estara sumando en la funcion dichas asignaciones 


#Si queremos que la función devuelva uno o varios valores, podemos usar return.

def funcion_suma(a, b): #aqui declaramos nuestra funcion que seria suma con las variables a, b
    return a + b        #aqui pedimos que nos retorne los valores de a + b 
suma = funcion_suma(3,5)#aqui declaramos que suma es igual a la funcion de sumar a +b
print("la suma es" , suma) #aqui pedimos que nos imprima el mensaje la suma es con el resultado de a + b

#VEAMOSLO CON OTROS OPERADORES MATEMATICOS

def funcion_multiplicacion (a, b): # aqui estamos diciendo que la funcion es tipo multiplicacion y con los valores a y b 
    print ("la multiplicacion", a * b) # aqui que nos imprima el resultado de dicha funcion
    
funcion_multiplicacion(5 , 5) # aqui le asignamos los valores 3 y 5 a la funcion multipliccion
# por lo tanto se estara multiplicando en la funcion dichas asignaciones 

#Si queremos que la función devuelva uno o varios valores, podemos usar return.
#igual se realiza sin importar el operador 

def funcion_multiplicacion(a, b):
    return a * b
suma= funcion_multiplicacion(5*5)
print("la multiplicacion es", funcion_multiplicacion)