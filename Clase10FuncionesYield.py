'''
Por último, yield está asociado a los generadores y 
las corrutinas, 
un concepto un tanto avanzado pero muy interesante.
En el siguiente generador vemos como 
se generan tres valores, obteniendo uno cada vez
que iteramos el generador.
'''

def generador(): 
    n = 1       #aqui declaramos la variable y el valor 
    yield n     # el generador mas la variable 
    
    n += 1      #aqui usamos la variable con el operadoe mas e igual al valor en este caso 1 
    yield n     # como anteriormente el generador y la variable
                
    n += 1      # cada vez que usamos el mismo bloque de codigo   
    yield n     # se repite la operacion y se itera en el resultado 

for i in generador(): # como vemos usamos i para la funcion del generador
    print(i) # por ultimo pedimos que nos imprima este resultado
    
    #Salida:
    1, 2, 3
    

def generador(): #declaramos la funcion en este caso es tipo generador
    nombre = 'jose' 
    yield nombre
    
    nombre = 'adrian'
    yield nombre 
    
    nombre = 'jose'
    yield nombre


for i in generador():
    print(i)
      
'''
Los generadores pueden ser usados para generar secuencias infinitas de valores, 
sin que tengan que ser almacenados a priori, siendo creados bajo demanda. 
Este es una utilidad muy importante trabajando con listas muy grandes, 
cuyo almacenamiento en memoria sería muy costoso.
'''
#ahaora vamos a hacer una lista con nombres y numeros como anteriormente
#pero esta vex que genere en la misma lista ambas variables el nombre con el numero 
# sin embargo al usar variables mixtas tenemos que tener en cuenta que ala hora de imprimir 
#cambia a la hora de declarar  la variable del generador para que las identifique por separado

def generador():
    nombre = 'jose'
    yield nombre
    n = 1
    yield n
    
    nombre = 'julia'
    yield nombre 
    n += 1
    yield n 
    

gen = generador()
for i in gen:
    print(i)