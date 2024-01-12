'''
Concurrencia: async, await
El uso de async y await nos permite ejecutar procesos de manera concurrente en vez de secuencial.
Imaginemos un proceso() que tarda 10 segundos en ejecutarse, ya que realiza una petición a
una base de datos que lo bloquea durante ese tiempo.
Sin esta herramienta, si quisiéramos ejecutar 3 veces el proceso tardaríamos 30 segundos, 
ya que por defecto se ejecutan de manera secuencial, hasta que uno no acaba no pasamos al siguiente.
'''
import asyncio #como en la clase 15 aqui se realiza la importancion de una biblioteca o extencion

async def proceso(id_proceso): #se declara la funcion que llamaremos proceso
    print("Empieza proceso:" , id_proceso) #imprimimos el mensaje de que empieza el proceso y la accion de la funcion
    await asyncio.sleep(10) #usamos el await y con la funcion asyncio y con el .slee (10) detenemos el proceso por 10 seg
    print("acaba proceso:" , id_proceso) #ahora vamos a imprimir la segunda accion y la funcion 
    
async def main(): #aqui estamos asignandole a dicha accion un main para poder llamarla 
    await asyncio.gather(proceso(1), proceso(2), proceso(3)) #aqui vamos finalmente lo que queremos que realice nuestra funcion llamada proceso
    
asyncio.run(main()) # aqui corremos nuestra funcion por medio del main anterior


'''
Sin embargo, creando una función async y usando await, 
podemos paralelizar la ejecución de los procesos, aprovechando el tiempo “muerto” mientras se retorna al await. 
En el siguiente ejemplo podemos ver como se tarda unos 10 segundos en ejecutar los 3 procesos.

'''