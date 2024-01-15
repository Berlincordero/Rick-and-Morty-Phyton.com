
#ESTA PARTE SOLO CONTIENE TEORIA 

'''
Estructuras de Control en Python
Antes de entrar a explicar las estructuras de control, vamos a ponernos un poco en contexto.

Un código es una secuencia de instrucciones, que por norma general son ejecutadas una tras otra.
Podemos verlo como una receta de cocina, en la que tenemos unos pasos a seguir. Empezamos por el principio, 
vamos realizando cada tarea, y una vez hemos llegado al final, hemos terminado. Nuestra receta en código podría ser la siguiente:

poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

Sin embargo, en muchas ocasiones no basta con ejecutar las instrucciones una tras otra desde el principio hasta llegar al final.
Puede ser que ciertas instrucciones se tengan que ejecutar si y sólo si se cumple una determinada condición. ¿Que pasa si nuestro
comensal es vegetariano? No hay problema, podemos usar el condicional if. Si no es vegetariano usamos pollo, de lo contrario zanahoria.


poner_agua_hervir()
echar_arroz_hervir()
if not vegetariano:
    cortar_pollo()
    freir_pollo()
    mezclar_pollo_arroz()
else:
    cortar_zanahoria()
    freir_zanahoria()
    mezclar_zanahoria_arroz()
    
Por otro lado, la receta que teníamos era para una persona. 
¿Qué pasa si queremos cocinar para 3? ¿Tenemos que escribir el código repetido 3 veces?

# Cocinamos para la primera persona
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

# Volvemos a cocinar para la segunda
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

# Y para la tercera
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()

Pero ¿y si queremos para 100? Te puedes ya imaginar que repetir el código tantas veces no parece ser la mejor idea.
Es aquí donde entran en juego el for y el while.
Estas estructuras de control nos permiten repetir un determinado bloque de código tantas veces como queramos.

# Repite lo que hay dentro 100 veces
for i in range(100):
    # Cocinamos la receta
    poner_agua_hervir()
    echar_arroz_hervir()
    cortar_pollo()
    freir_pollo()
    mezclar_pollo_arroz()


Como puedes ver, el código anterior haría lo mismo que copiar y pegar la receta 100 veces, pero es mucho más compacto y elegante.

Sabido esto, ya estas en condiciones de empezar a leer este capítulo, donde aprenderás básico conceptos como el if/else/for/while y también algo más avanzados,
como lo son los iteradores, clases iterables y uso del break/continue/try.


'''

