#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def getMultiplesListBelowNumber(list, limit):
    res = []
    i = 1
    while i < limit:
        for j in list:
            if i % j == 0 and i not in res:
                res.append(i)
        i = i + 1
    return res


def sumListNumbers(list):
    res = 0
    for i in list:
        res = res + i
    return res

multiples = getMultiplesListBelowNumber([3,5], 1000)
sumMultiples = sumListNumbers(multiples)
print (sumMultiples)
