'''
For anidados
Es posible anidar los for, es decir, meter uno dentro de otro.
Esto puede ser muy útil si queremos iterar algún objeto
que en cada elemento, tiene a su vez otra clase iterable.
Podemos tener por ejemplo, una lista de listas, una especie
de matriz.
'''
# tome en cuenta que esta clase es muy importante podemos 
# ver como se puede iteractuar y crear matrices usando el for 

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
    
# si iteramos usando solo un for iteraremos con toda la lista
# pero no a los elementos individuales 

for i in lista:
    print(i)

'''
Si queremos acceder a cada elemento individualmente,
podemos anidar dos for. Uno de ellos se encargará de iterar 
las columnas y el otro las filas.
'''
lista = [[56, 34, 5],
         [90, 91, 92],
         [11, 65, 78]]


for i in lista: # de esta forma se esta accediendo individualmente a cada elemento y no como conjunto
    for j in i: # esto permitira que nos muestre i en una lista pero en tal lista por linea solo habra un numero siendo asi individual su acceso
        print(j)# por lo tanto nos imprimira una lista con estos numero de la variable


# otros ejemplos del for
'''
Iterando cadena al revés. Haciendo uso de [::-1] 
se puede iterar la lista desde el último al primer elemento.
'''


texto = "Python"
for i in texto[::-1]:
    print(i)
    

numeros = 1, 2, 3, 4, 5 
for j in numeros[::-1]:
    print(j)

'''
Itera la cadena saltándose elementos.
Con [::2] vamos tomando un elemento si y otro no.
'''
texto = "Python"
for i in texto[::2] # recordemos que si queremos imprimir al reves o al derecho es igual que con los numeros se hace con positivo y negativo
    print(i)


numero = 1, 2, 3, 4, 5
for j in numero[::2]:
    print(j)

# Un ejemplo de for usado con comprehensions lists.

print(sum(i for i in range(10)))

