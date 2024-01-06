'''
 son valores que pueden ser asignados a variables, 
 siendo los dos primeros booleanos y el último algo parecido al null de otros lenguajes de programación.
'''
#False
#Si realizamos una comparación usando el operador relacional == se nos devolverá True o False.
#En este caso veremos como fun
#funciona con el false 

X = (5 == 1) # en esta accion decimos que x es igual a la variable 5 es igual a 1 
print(X)     # Sin embargo esta afirmacion es falsa y nos retornara un false 
# En este caso nos devolvera un false 

#True 
#Ahora veremos como funciona el true (cuando una accion es verdadera)

x = (5 == 5) # En este caso la afirmacion es correcta 5 es igual igual a 5 
print(x)   # simplificando lo anterior lo que quiere decir es que el numero es igual al otro
# por lo tanto nos a a devolver un true

#Asignandole un true a una varible
#También podemos asignar nosotros True a una variable.
#COMO?

x = True   # como sucede en este caso le asignamos el true a esta variable
if x:      # si x es verdadera imprima Phyton en este caso ya estamos asigando por default que es verdadera
    print("Phyton!")
    # siendo la accion verdadera nos imprimira Phyton
    

#None
'''
Por otro lado None se devuelve por defecto cuando una función no cuenta con un return.
'''

def mi_funcion(): # En este caso vemos nuestra funcion que no returna ninguna funcion en si
    pass          # que quiere decir esto que la no contar con un return no devolvera la funcion 
print(mi_funcion()) # por lo tanto el resultado sera ninguno(None)

