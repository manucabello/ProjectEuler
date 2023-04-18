#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe un programa en Python que le pida al usuario un número entero positivo y luego calcule la suma de todos los números pares desde el 2 hasta el número ingresado.
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
