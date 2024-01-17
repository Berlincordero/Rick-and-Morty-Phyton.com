'''
Uso de else y elif
Es posible que no solo queramos hacer algo si una determinada 
condición se cumple, sino que además queramos hacer algo de lo 
contrario.Es aquí donde entra la cláusula else. La parte del
if se comporta de la manera que ya hemos explicado, con la diferencia 
que si esa condición no se cumple,se ejecutará el código presente dentro del else.
Nótese que ambos bloque de código son excluyentes, se entra o en uno o en otro,
pero nunca se ejecutarán los dos.
'''
# Uso del else 

x = 5 # se declara la variable y su valor 
if x == 5: # si x es igual e igual a 5
    print("Es 5") # imprima es 5

else: # sino 
    print("No es 5") #imprima no es 5
    

# Ejemplo #2

nombre = 'pedro'  # tenemos la variable nombre que nos aloja el nombre pedro

if nombre == 'pedro': # si el nombre es igual e igual a pedro
    print('el nombre es pedro') # imprima el nombre es pedro

else: # sino
    print('no lo es') # imprima no lo es 


     
    
