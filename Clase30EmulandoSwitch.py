'''
Emulando switch en Python
Una forma de tener una especie de switch en Python 
es haciendo uso de un diccionario.
Por lo tanto podríamos convertir el siguiente código.
'''
operador = 1
a = 3 
b = 2
def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None # como vemos al no cumplirse ninguna de las condiciones antetiores no devolvera ningun valor.

# Otro ejemplo: 
opera2 = operador
a = 3 
b = 2

def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)