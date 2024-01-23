'''
Introducción al switch
Ya sabemos que el uso del if junto con else y elif
nos permite ejecutar un código determinado dependiendo
de una condicion, como podemos ver en el siguiente código.
'''
condicion = 4

if condicion == 1:
    print("Haz a")
elif condicion == 2:
    print("Haz b")
elif condicion == 3:
    print("Haz c")
else:
    print("Haz d")
    
#################################################################################################################################################################################################
# Otro Ejemplo del uso del switch pero no en python ya que switch la variable como tal no existe 
'''
La misma funcionalidad se podría escribir de la siguiente manera haciendo uso del switch.
Como puedes ver su uso tal vez resulte algo más limpio, 
y de hecho en determinadas ocasiones es más rápido.

// Ojo, esto no es Python
switch(condicion) {
  case 1:
    // haz a
    break;
  case 2:
    // haz b
    break;
  case 3:
    // haz c
    break;
  default:
    // haz x
}

Pero tenemos un pequeño problema. 
En Python no existe el switch, por lo que si intentas 
ejecutar el código anterior, tendrás un error.
Uno tal vez podría decir: bueno, que más da, uso 
if/elif/else y ya esta. La verdad que en la mayoría 
de los casos, sería indiferente usar if o switch,
pero si analizamos el comportamiento que existe por debajo, 
funcionan de manera distinta.
A pesar de que en Python no existe, 
te damos un truco que puede en cierto modo emular
su funcionamiento.

'''
###########################################################################################################################################################
'''
Diferencia if y switch
Una de las principales diferencias, 
es que usando if con elif, no todos los bloques
tienen el mismo tiempo de acceso.
Todas las condiciones van siendo evaluadas hasta 
que se cumple y se sale. Imaginemos que tenemos
100 condiciones.

'''
condicion = 100
if condicion == 1:
    print("1")
elif condicion == 20:
    print("2")
elif condicion == 100:
    print("3")

else :
    print("ninguna")

'''
El tiempo de ejecución será distinto si la condicion 
es 1 o es 70 por ejemplo:

Si es 1: Se evalúa el primer if, y como se cumple la condición
se ejecuta y se sale.
Si es 70: Se va evaluando cada condición, hasta llegar al 70.
Es decir, tienen que evaluarse 70 condiciones.
Sin embargo, en el switch todos los elementos tienen
el mismo tiempo de acceso. Esto se debe a que por debajo
esta normalmente implementado con lookup tables.

Si trabajamos con un gran número de condiciones,
el uso del switch sobre el if podría notarse.

Dado que en Python no tenemos esta herramienta,
te explicamos un truco para simularlo.
No obstante, si realmente te preocupan estas 
micro optimizaciones, tal vez no deberías usar Python.
'''
