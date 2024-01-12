# vamos a leer un poquito en que consiste el duck typing
'''
Duck Typing en Python
El duck typing o tipado de pato es un concepto relacionado con la programación que 
aplica a ciertos lenguajes orientados a objetos, y que tiene origen en la siguiente frase:

If it walks like a duck and it quacks like a duck, then it must be a duck

Lo que se podría traducir al español como. 
Si camina como un pato y habla como un pato, entonces tiene que ser un pato.
¿Y qué relación tienen los patos con la programación? Pues bien, se trata de un símil en el que los patos son objetos y hablar/andar métodos. 
Es decir, que si un determinado objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante.
Dicho de otra manera, no mires si es un pato. Fíjate si habla como un pato, camina como un pato, etc. Si 
cumple con todas estas características, ¿no podríamos acaso decir que se trata de un pato?

Don’t check whether it is-a duck: check whether it quacks-like-a duck, walks-like-a duck, etc, etc, depending on exactly what subset of duck-like behavior you need to play your language-games with. (comp.lang.python, Jul. 26, 2000) — Alex Martelli

El concepto de duck typing se fundamenta en el razonamiento inductivo, donde una serie de premisas apoyan la conclusión, pero no la garantizan. Si vemos a un animal que parece un pato, habla como tal y anda como tal, 
sería razonable pensar que se trata de un pato, pero sin un test de ADN nunca estaríamos al cien por cien seguros.
Una vez entendido el origen del concepto, veamos lo que realmente significa esto en Python. En pocas palabras, a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos.
Definamos una clase Pato con un método hablar().
'''
