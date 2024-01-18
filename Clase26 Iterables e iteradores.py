'''
Iterables e iteradores
Para entender al cien por cien los bucles for, 
y como Python fue diseñado como lenguaje de programación, 
es muy importante entender los conceptos de iterables e
iteradores. Empecemos con un par de definiciones:

Los iterables son aquellos objetos que como su nombre indica
pueden ser iterados, lo que dicho de otra forma es, que
puedan ser indexados. 
Si piensas en un array (o una list en Python), podemos 
indexarlo con lista[1] por ejemplo, por lo que sería un
iterable.

Los iteradores son objetos que hacen referencia a
un elemento, y que tienen un método next que permite hacer 
referencia al siguiente.

'''
'''
Ambos son conceptos un tanto abstractos y que pueden ser 
complicados de entender. Veamos unos ejemplos. Como hemos
comentado, los iterables son objetos que pueden ser iterados
o accedidos con un índice. Algunos ejemplos de iterables en 
Python son las listas, tuplas, cadenas o diccionarios. 
Sabiendo esto, lo primero que tenemos que tener claro es 
que en un for, lo que va después del in deberá ser siempre 
un iterable.

#for <variable> in <iterable>:
#    <Código>

Tiene bastante sentido, porque si queremos iterar una variable,
esta variable debe ser iterable, todo muy lógico.
Pero llegados a este punto, tal vez de preguntes
¿pero cómo se yo si algo es iterable o no?.
Bien fácil, con la siguiente función isinstance() podemos 
saberlo. No te preocupes si no entiendes muy bien lo que
estamos haciendo, fíjate solo en el resultado, True significa
que es iterable y False que no lo es.

'''
'''
from collections import Iterable
lista = [1,2,3,4] # como vemos este es un objeto iterable o mejor dicho indexable como una lista de numeros
cadena = "PYTHON" # como vemos otro objeto indexable es una cadena de caracteres como lo es una palabra
numero = 10 # sin embargo aunque la variable esta almacenando 10 numeros estos no estan en una lista sino en un numero entero por lo tanto no podemos indexarlos

print(isinstance(lista, Iterable)) #True
print(isinstance(cadena, Iterable)) # True
print(isinstance(numero, Iterable)) # False
'''
'''
Por lo tanto las listas y las cadenas son iterables,
pero numero, que es un entero no lo es. Es por eso por lo 
que no podemos hacer lo siguiente, ya que daría un error.
De hecho el error sería TypeError: int' object is not iterable.

numero = 10
#for i in numero:
#    print(i)

>ITERADORES<
Una vez entendidos los iterables, veamos los iteradores.
Para entender los iteradores, es importante conocer la función
iter() en Python. Dicha función puede ser llamada sobre un 
objeto que sea iterable, y nos devolverá un iterador como 
se ve en el siguiente ejemplo.
'''
lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828>
print(type(it)) #<class 'list_iterator'>

'''
Vemos que al imprimir it es un iterador, de la clase 
list_iterator. Esta variable iteradora, hace referencia 
a la lista original y nos permite acceder a sus elementos
con la función next(). Cada vez que llamamos a next() sobre
it, nos devuelve el siguiente elemento de la lista original.
Por lo tanto, si queremos acceder al elemento 4, tendremos 
que llamar 4 veces a next(). Nótese que el iterador empieza 
apuntando fuera de la lista, y no hace referencia al primer
elemento hasta que no se llama a next() por primera vez.

'''

lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it

