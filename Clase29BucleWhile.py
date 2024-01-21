'''
Bucles while
Anteriormente hemos visto el uso del if y el for 
para modificar el flujo de ejecución del código. 
A continuación vemos otra forma de hacerlo con el while.
'''

'''
While
El uso del while nos permite ejecutar una sección de código
repetidas veces, de ahí su nombre. El código se ejecutará 
mientras una condición determinada se cumpla. 
Cuando se deje de cumplir, se saldrá del bucle y se 
continuará la ejecución normal. Llamaremos iteración a
una ejecución completa del bloque de código.

Cabe destacar que existe dos tipos de bucles,
los que tienen un número de iteraciones no definidas,
y los que tienen un número de iteraciones definidas
. El while estaría dentro del primer tipo.
Mas adelante veremos los for, que se engloban en el segundo.
'''
# Veamos

x = 5
while x > 0: # hasta que llegue a 0 la condicion se habra cumplido dentro de bucle
    x -= 1   # si el numero no es igual a 0 entonces x va a hacer menos o igual a uno que quiere decir esto que se le restara a 5 menos 1 hasta que se cumpla esta condicion 
    print(x) # por lo tanto imprimira dicho resultado hasta llegar a o


'''
En este caso se entra al bloque de código 5 veces,
hasta que en la sexta, x vale cero y 
por lo tanto la condición ya no se cumple. 
Por lo tanto el while tiene dos partes:

La condición que se tiene que cumplir para que se ejecute 
el código.
El bloque de código que se ejecutará mientras la condición se cumpla.

Ten cuidado ya que un mal uso del while puede dar lugar a
bucles infinitos y problemas. Cierto es que en algún caso 
tal vez nos interese tener un bucle infinito, pero salvo 
que estemos seguros de lo que estamos haciendo, hay que 
tener cuidado. Imaginemos que tenemos un bucle cuya
condición siempre se cumple. Por ejemplo, si ponemos
True en la condición del while, siempre que se evalúe
esa expresión, el resultado será True y se ejecutará 
el bloque de código. Una vez llegado al final del bloque,
se volverá a evaluar la condición, se cumplirá, y vuelta 
a empezar. No te recomiendo que ejecutes el siguiente código,
pero puedes intentarlo.

# No ejecutes esto, en serio
while True:
    print("Bucle infinito"
    
'''
'''
Es posible tener un while en una sola línea,
algo muy útil si el bloque que queremos ejecutar es corto.
En el caso de tener mas de una sentencia, las debemos separar
con ;.
'''

x = 5
while x > 0: x -= 1; print(x) #como en la condicion igual see le de la misma forma
# mientras x sea mayor a 0 ...entonces.. x menos o igual a 1... imprimame x 
# por lo tanto restara 1 en cada paso hasta llegar a 0 que es donde se cumple esta condicion

#Eliminando elementos usando el While
'''
También podemos usar otro tipo de operación dentro del while,
como la que se muestra a continuación.
En este caso tenemos una lista que mientras no este vacía,
vamos eliminando su primer elemento.
'''
x = ["uno", "dos", "tres"]
while x:     # mientras x 
    x.pop(0) # se elimine hasta llegar a 0
    print(x) # imprima a x (resultado)



nombres = [ "adrian", "marco", "ramon"]
while nombres:
    nombres.pop(0)
    print(nombres)

Characters = ["A", "B", "C", "D", "E"]
while Characters:
    Characters.pop(0)
    print(Characters)
# como vemos podemos usarlo para distintos ejemplos y cantidades de elementos