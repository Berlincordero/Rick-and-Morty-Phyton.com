'''
Ejemplos Duck Typing
'''
'''
Ejemplo len()
Podemos ver el duck typing en todo su esplendor con la función len(). Dicha función lo único que realiza por debajo es llamar al método mágico __len__(). Definamos dos clases:

Foo implementa el método __len__().
Bar no lo implementa.
'''
'''
nota: 
En Python, len es una función integrada que se utiliza para obtener la longitud 
(número de elementos) de un objeto iterable o la cantidad de caracteres en un objeto 
de texto (cadena).
Donde objeto puede ser cualquier objeto iterable, como una lista, 
una tupla, una cadena, un diccionario, etc.
'''
class Foo(): #foo implementa el metodo en la clase
    def __len__(self):
        return 99

class Bar(): # el bar no lo implementa la accion como lo vimos anteriormente 
    pass

'''
Como ya hemos explicado, a la función len() no le importa el tipo del objeto que se le pase,
siempre y cuando tenga el método __len__() implementado. Por ello, en el segundo caso falla.
'''
# como vemos en uno da el resultado ya que se le esta pasando un objeto
# en el otro aunque igual se le esta pasando el metodo len pero no se le esta pasando un bojeto

print(len(Foo())) #99
print(len(Bar())) #Error

'''
Ejemplo multiplicar
Por otro lado, cuando hacemos una multiplicación utilizando el operador aritmético * el resultado depende de los tipos que estemos usando.

No es lo mismo multiplicar dos enteros que un entero y cadena.
'''
print(3*3) #9
print(3*"3") #333

# Una vez más, podemos ver el duck typing en Python. Simplemente se busca que los objetos a
# la izquierda y derecha del * tengan implementado el __rmul__ o __mul__.

#IMPORTANTE
'''
Conclusiones
Python es un lenguaje que soporta el duck typing, lo que hace que el tipo de los objetos no sea tan relevante, siendo más importante lo que pueden hacer (sus métodos).
Otros lenguajes como Java no soporta el duck typing, pero se puede conseguir un comportamiento similar cuando 
los objetos comparten un interfaz (si existe herencia entre ellos). Este concepto relacionado es el polimorfismo.
El duck typing está en todos lados, desde la función len() hasta el uso del operador *.
'''