#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe una función en Python que tome como entrada una lista de números enteros y devuelva una nueva lista que
contenga solo los números impares de la lista original en orden inverso al que aparecen en la lista original.

Además, la función debe imprimir por pantalla la cantidad de números impares encontrados en la lista original.

Por ejemplo, si la lista original es [2, 5, 6, 7, 8, 9], la nueva lista debería ser [9, 7, 5]
"""


"""
Method to get the odd numbers in a list and reverse them.
- Args:
    param1: The list with the numbers
- Returns:
    res: The reverse list with the odd numbers
"""
def getOddAndReverse(my_list):
    res = []
    for i in my_list:
        if i % 2 != 0:
            res.append(i)
    res.reverse()
    print (len(res))
    return res

print (getOddAndReverse([2,5,6,7,8,9]))