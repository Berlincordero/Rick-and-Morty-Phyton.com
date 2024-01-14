'''
¿Y qué pasa si usamos otros objetos que no son de la clase Pato? Pues bien,
como hemos dicho, a la función llama_hablar() le da igual el tipo.
Lo único que el importa es que el objeto tenga el método hablar().

Definamos tres clases de animales distintas que implementan el método hablar().
Nótese que no existe herencia entre ellas, son clases totalmente independientes. 
De haberla estaríamos hablando de polimorfismo.
'''
class Perro:
    def hablar(self):
        print("¡Guau!")

class Gato:
    def hablar(self):
        print("¡Miau!")

class Vaca:
    def hablar(self):
        print("¡Muu!")

def llama_hablar(animal):
    animal.hablar()

# Y como es de esperar la función llama_hablar() funciona correctamente con todos los objetos

# Ejemplos de llamadas
llama_hablar(Perro())  # Imprimirá: ¡Guau!
llama_hablar(Gato())   # Imprimirá: ¡Miau!
llama_hablar(Vaca())   # Imprimirá: ¡Muu!
