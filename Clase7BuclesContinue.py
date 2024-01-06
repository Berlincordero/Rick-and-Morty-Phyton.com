'''
El continue salta hasta el final del bloque, 
dejando sin ejecutar lo restante, pero continúa en la siguiente iteración.
'''

for i in range(3):
    if i == 1:     #como observamos el continue es para que se salte a
        continue   # la ultima accion que en dicho caso imprimi la accion condicional
    print(i) 
    
    #Transcripcion 
    '''
    para i en rango de 3 
    si i es igual a 1 
    continue e imorima i 
    que este caso imprimira el rango de alcance exceptuando el 3 mismo 
    que seria lo que esta dentro de este rango
    '''
    
