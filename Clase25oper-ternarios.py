'''
Operador ternario
El operador ternario o ternary operator es una herramienta 
muy potente que muchos lenguajes de programación tienen. 
En Python es un poco distinto a lo que sería en C, pero el 
concepto es el mismo. Se trata de una cláusula if, else que
se define en una sola línea y puede ser usado por ejemplo, 
dentro de un print().
'''
d = 5
print("es 5" if d == 5 else "No lo es")

letra = 'a'
print("es la a" if letra == 'a' else "no lo es")

nombre = "joel" # como se ve se coloca la variable y se le declara dicho valor o cadena de letras
print("es el nombre" if nombre == "luis" else "no lo es") # dentro del prin se pueden declara las funciones haciendolo mas compacto en una sola linea en vez de varias

'''
Existen tres partes en un operador ternario, que son exactamente
iguales a los que había en un if else. Tenemos la condición
a evaluar, el código que se ejecuta si se cumple, y el
código que se ejecuta si no se cumple. En este caso, tenemos 
los tres en la misma línea.
'''
# [código si se cumple] if [condición] else [código si no se cumple]

'''
Siguiendo el ejemplo anterior, en el siguiente código
intentamos dividir a entre b. Si b es diferente a cero,
se realiza la división y se almacena en c, de lo contrario
se almacena -1. Ese -1 podría ser una forma de indicar que 
ha habido un error con la división.
'''

a = 10 # colocamos el valor a la variable 
b = 5  # colocamos el valor a la variable 
c= a/b if b!=0 else -1 # dentro de la variable declaramos en este caso nuestra operacion seguido de nuestra condcion
print(c) # imprimimos la variable que la almacena 


