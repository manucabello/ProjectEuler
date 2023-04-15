#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Ejercicio1: Escribe un programa que imprima un patrón de asteriscos. El programa debe solicitar al usuario un número
entero, que indicará la cantidad de filas que tendrá el patrón. Cada fila debe imprimir un número de asteriscos igual
al número de la fila. Por ejemplo, si el usuario introduce 5, el patrón debe verse así:
*
**
***
****
*****
"""

def pyramid(num):
    if type(num) == int:
        lista = list(range(0,num))
        res = []
        for i in lista:
            aux = ""
            while len(aux) <= i:
                aux = aux+"*"
            res.append(aux)
        for i in res:
            print (i)
        return True
    else:
        print ("El valor introducido no es válido")
        return False

num = int(input("Introduzca el número de filas: "))
pyramid(num)