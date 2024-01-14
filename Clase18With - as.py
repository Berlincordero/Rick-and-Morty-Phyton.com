'''
Context Managers: with, as
El uso de -with y as- es muy utilizado a la hora de manejar ficheros,
pero en realidad pertenecen a los context managers o gestores de contexto,
un concepto algo avanzado.
'''
with open('fichero.txt', 'r') as file: # aqui estamos abriendo un fichero txt y en la extencion o archivo 'r'
    print(file.read()) # ahora pedimos que nos imprima dicha lectura de este archivos
       