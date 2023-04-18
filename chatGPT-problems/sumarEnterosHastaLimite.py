#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe un programa en Python que le pida al usuario un número entero positivo y luego calcule la suma de todos los
números pares desde el 2 hasta el número ingresado.
"""


"""
Calculates the sum of all positive integers up to and including a given number.
- Args:
    num (int): a positive integer greater than or equal to 2
- Raises:
    If num is less than 2, the function prompts the user to enter a positive integer greater than or equal to 2 and
    returns the sum of integers up to the new input value.
- Returns:
    res (int): An integer representing the sum of all positive integers up to and including num
"""
def sumaEnterosHastaLimite(num):
    if num >= 2:
        res = 0
        i = 2
        while i <= num:
            res = res + i
            i = i + 1
        return res
    else:
        print("El número ingresado debe ser mayor o igual a 2.")
        num = int(input("Ingrese un número entero positivo: "))
        return sumaEnterosHastaLimite(num)


num = int(input("Ingrese un número entero positivo mayor o igual a 2: "))
print(sumaEnterosHastaLimite(num))
