'''
Por otro lado, podemos usar pass cuando no queramos definir la función,
es decir si la queremos dejar en blanco por el momento.
Nótese que también puede ser usado en clases, estructuras de control, etc.
'''
#Ejemplo
def funcion_suma(a, b):
    pass # que significa esto que la funcion nos la va a generar en blanco y pasara ala siguiente funcion.

#veamos como funciona en comparacion una funcion completa

def funcion_suma(a,b):
    print("la suma es"  , a + b)
    
suma = funcion_suma (3 , 5)#aqui vemos una funcion completa a comparacion con la otra 
#y si ejecutamos el codigo veremos como pasara a la siguiente funcion
#dandonos solo el resultado de funcion que si esta completa.