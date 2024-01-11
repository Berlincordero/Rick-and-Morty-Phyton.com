'''
Las palabras clave assert, try, except, finally y raise están relacionadas con las excepciones,
y nos permiten tratar el qué hacer cuando las cosas no salen como esperamos. 
El siguiente código intenta hacer un cast de cadena a entero, manejando un posible error.

Si x="10" el casteo se realiza sin problemas, ya que es posible representar esa cadena como un entero.
Sin embargo hay que estar preparados siempre para lo peor.
Si x="a" no se podría hacer int() y tendríamos un error. 
Si no manejamos este error, el programa se pararía, y esto no es algo deseable. 
El uso de try, except y finally nos permite controlar dicho error y actuar en consecuencia sin que el programa se pare.

'''

x = "5"
valor = None
try:
    valor = int(x)
except Exception as e:
    print("hubo un error:", e)
finally:
    print("el valor es", valor)
    
#######################################################
'''
En este ejemplo, la función dividir intenta realizar la división a / b. Utiliza assert para verificar que el divisor (b) no sea cero. 
Si el divisor es cero, se genera una excepción con raise. El bloque try maneja las operaciones dentro de él,
y el bloque except maneja la excepción en caso de una división por cero. El bloque finally se ejecuta siempre,
independientemente de si hay una excepción o no, y se utiliza aquí para imprimir un mensaje indicando que la operación de división ha finalizado.
'''

def dividir(a, b):
    try:
        assert b != 0, "El divisor no puede ser cero"
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero.")
        return None
    finally:
        print("Operación de división finalizada.")

# Ejemplo de uso
numerador = 10
divisor = 2

resultado = dividir(numerador, divisor)
if resultado is not None:
    print(f"El resultado de {numerador} dividido por {divisor} es: {resultado}")