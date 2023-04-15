#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe un programa que solicite al usuario ingresar un número entero positivo y luego calcule la suma de los dígitos
de ese número.

Por ejemplo, si el usuario ingresa el número 12345, el programa debe calcular la suma 1 + 2 + 3 + 4 + 5 = 15.

El programa debe imprimir en pantalla la suma de los dígitos del número ingresado.
"""


"""
Method to sum all digits of a number
- Args:
    param1: Number to sum its digits
- Returns:
    res: The sum of the digits of the number
"""
def sumaDigitos(num):
    res = 0
    while num > 0:
        res = res + (num % 10)
        num = num // 10
    return res

num = int(input("Introduce un número para sumar sus dígitos: "))
print (sumaDigitos(num))