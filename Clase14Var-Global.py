'''
El uso de global permite realizar lo siguiente, y de no usarlo tendríamos un UnboundLocalError.
Aunque puede resultar muy útil, mucho cuidado con las variables globales.
'''

a = 0 # la variable aqui esta deinida con el valor de cero (ninguno o None)

def suma_uno(): # aqui vemos la funcion definida como suma uno como asi mismo define lo que hace la operacion por lo tanto mas facil de leer
    global a  # tenemos la variable global que encasulara a la variable (a)
    a = a + 1 # por lo tanto a es a mas 1 pero recordando que el valor de a es 0
    
suma_uno() #llamamos la funcion suma uno
print(a)   #finalmente imprimimos nuestra variable que de tipo global
# por lo tanto la salida debe ser uno