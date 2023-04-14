#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""


"""
Method to descompose a number into prime factors
- Args:
    param1: The number to desompose in prime factors
- Returns:
    res: The prime factors of the number
"""
def getPrimeFactors(num):
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


"""
Method to get the LCM (Low Commun Multiple) of all numbers up to the limit value
- Args:
    param1: The limit value
- Returns:
    res: The LCM of the numbers
"""
def getLCM(limit):
    res = 1
    primeFactors = []
    i = 2
    while i <= limit:
        primeFactors.append(getPrimeFactors(i))
        i = i + 1
    mcm = {}
    for numFactor in primeFactors:
        for factor in numFactor:
            if factor in mcm:
                mcm.update({factor: max(numFactor.count(factor), mcm[factor])})
            else:
                mcm.update({factor: numFactor.count(factor)})
    for key in mcm:
        res = res * (key**mcm[key])
    return res

# Print the LCM of the numbers from 1 to 20
print (getLCM(20))
