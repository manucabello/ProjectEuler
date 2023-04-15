#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe un programa que imprima la tabla de multiplicar del 1 al 10. El programar debe utilizar dos loops anidados
para recorrer los números del 1 al 10 y multiplicarlos entre sí. El resultado de cada multiplicación debe imprimirse
en una nueva línea. Por ejemplo, el resultado de la multiplicación de 2x3 debe imprimirse en una nueva línea, y el
resultado de la multiplicación de 4x5 debe imprimirse en otra línea.
"""

def tablaMultiplicar():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print (str(i)+'x'+str(j)+'='+str(i * j))
            j = j + 1
        i = i + 1
        print ()

tablaMultiplicar()