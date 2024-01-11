'''
El uso de lambda nos permite crear funciones lambda, una especie de funciones “para vagos”. Dichas funciones no tienen un nombre per se, salvo asignado explícitamente.
aque se refiere esto que a la estructura de la funcion se comprime toda en el print
por lo tanto es un poco complicado pero simplificada
'''
#Ejemplo

print("la suma es" , (lambda a, b: a + b)(3,5))

#Ejemplo

print("la multiplicacion es", (lambda a, b: a* b)(3,5))


#Ejemplo

print("la resta" , (lambda a, b: a - b )(10 , 5))

#Ejemplo

print("la division es" , (lambda a, b: a / b)(15 , 3))

#Ejemplo

print("la suma es" , (lambda a , b: a + b)(7 , 7))

#como vemos en todas las funciones anteriores se resume en imprimir
#dentro del mismo print el mensaje y agregando la opercaion correspondiente
#como se dijo anteriormente es una funcion de compactimiento