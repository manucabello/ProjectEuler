#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""


"""
Method to get the GCM (Greatest Common Divisor) of two numbers
- Args:
    param1: number 1
    param2: number 2
- Returns
    res: The GCM of param1 and param2
"""
def getGCD(a,b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    res = a
    return res

"""
Method to get the LCM (Low Commun Multiple) of two numbers
- Args:
    param1: number 1
    param2: number 2
- Returns
    res: The LCM of param1 and param2
"""
def getLCM(a,b):
    res = (a * b) // getGCD(a,b)
    return res

"""
Method to get the LCM (Low Commun Multiple) of all numbers up to the limit value
- Args:
    param1: The limit value
- Returns:
    res: The LCM of the numbers
"""
def getLCM_list(num):
    res = 1
    for i in range(2, num + 1):
        res = getLCM(i, res)
    return res

print (getLCM_list(20))