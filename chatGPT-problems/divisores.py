#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe una función en Python llamada numDivisores(num) que reciba como argumento un número entero positivo num y
devuelva la cantidad de divisores que tiene ese número (sin contar el 1 y el propio número).

Por ejemplo:
    Si se llama a la función numDivisores(10), debería devolver 2 (ya que 10 tiene dos divisores propios: 2 y 5).

Puedes suponer que el número ingresado siempre será un entero positivo mayor que 1.
"""

"""
Calculates the number of integer divisors of a given positive integer.
- Args:
    num (int): a positive integer for which to count divisors
- Returns:
    rest (list): An integer representing the number of divisors of num
"""
def numDivisores(num):
    res = 1
    checked = []
    factors = descomponerEnFactores(num)
    for factor in factors:
        if factor not in checked:
            checked.append(factor)
            res = res * (factors.count(factor) + 1)
    return res


"""
Method to descompose a number into prime factors
- Args:
    num (int): The number to desompose in prime factors
- Returns:
    res (list): The prime factors of the number
"""
def descomponerEnFactores(num):
    res = []
    i = 2
    while i * i <= num:
        if num % i:
            i = i + 1
        else:
            num = num // i
            res.append(i)
    res.append(num)
    return res


print(descomponerEnFactores(2520))
print(numDivisores(2520))