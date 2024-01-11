'''
El uso de nonlocal es útil cuando tenemos funciones anidadas. 
El el siguiente ejemplo podemos ver como cuando funcion_b modifica x,
también afecta a la x de la funcion_a, ya que la hemos declarado como nonlocal. 
Te invitamos a que elimines el nonlocal y veas el comportamiento.
'''

def funcion_a(): #un aspecto importante a tomar en cuenta en python se utiliza _ para asignar el nombre de la funcion
    x = 10  #aqui declaramos que x tiene el valor de 10
    
    
    def funcion_b(): #Definimos la segunda funcion que seria b.
        nonlocal x #aqui es donde usamos la variable o palabra reservada como desee nonlocal 
        x = 20 # a x se le esta asignando el valor de 20 pero dentro de la funcion de b 
        print("funcion_b" , x) #aqui imrímimos el mesaje seguido de la variable en este caso x
        
    funcion_b() # llamamos a la funcion b
    print("funcion_a" , x) # y imprimimos el msj de la funcion en este caso a y eñ valor de la variable 
    # tomando en cuenta que x  de la funcion a fue declarada nonlocal en la funcion b 
    #por lo tanto ahora el valor de x es el de la x de la funcion b en este caso es 20
    
funcion_a() #llamamos la funcion (a)