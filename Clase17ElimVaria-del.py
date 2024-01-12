'''
Eliminar variables: del
El uso de del nos permite eliminar una variable del scope, 
pudiendo resultar útil cuando trabajamos con variables que almacenan gran cantidad de datos. 
Es una manera explícita de indicar que ya no queremos una variable, 
pero no olvidemos que Python tiene gargabe collector.
'''
#que significa esto que podemos eliminar el valor que le ponemos a una variable

a = 15 # aqui le asignamos el valor a la variable 
del a  # aqui usamos el del para eliminar al valor de a dejam¿ndola como una variable indefinida
print(a) # aqui pedimos que nos imprima a (a) 
# acontinuacion como no esta definida nos dara un mensaje de error     
#Salida: NameError: name 'a' is not defined