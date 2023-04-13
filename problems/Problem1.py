#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


"""
Method to obtain the multiples without repetition below a limit value of a list of numbers
- Args:
    param1: The list of numbers to get their multiples of
    param2: The limit value of the multiples to obtain
- Returns:
    res: The list with the multiples below the param2 value of the numbers included in the param1 list
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


"""
Method to get the sum of all the numbers of a list
- Args:
    param1: The list of numbers to sum
- Returns:
    res: The sum of all the elements of the list
"""
def sumListNumbers(list):
    res = 0
    for i in list:
        res = res + i
    return res

# Get the multiples below 1000 of 3 or 5
multiples = getMultiplesListBelowNumber([3,5], 1000)

# Sum the multiples
sumMultiples = sumListNumbers(multiples)

# Print result
print (sumMultiples)
