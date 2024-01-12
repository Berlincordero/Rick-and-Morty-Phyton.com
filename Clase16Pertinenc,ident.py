'''
Pertenencia e Identidad: in, is
El uso de in nos permite saber si un determinado elemento está en una clase iterable(Capaz de repetirse), 
devolviendo True en el caso de que sea cierto.
'''
lista = ["a" , "b", "c"] # el elemento es iterable debido que no hay una accion que defina las veces que se puede usar dento de la lista 
print("a" in lista) # en otras palabras hasta que se defina esta accion se puede repetir cuantas veces sea necesario 
                    # siendo un elemento repetible.

#Salida: True 

########################################################################################################################################################

'''
El uso de is nos permite saber si dos variables apuntan en realidad al mismo objeto. 
Por debajo se usa la función id() y es 
importante notar que la igualdad == no implica que is sea True.
'''

a = [1, 2]
b = [1, 2]
c = a 

print(a is b) # esta afirmacion es falsa por que aunque ambas variables tengan almacenados los mismos valores no se llaman igual o si?
print(a is c) # esta afirmacion es correcta ya que c se decalra con el valor de (a)