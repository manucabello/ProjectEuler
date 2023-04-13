#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


# Using successive division method
def getPrimeFactors(num):
    res = []
    i = 2
    while i * i <= num:
        if num % i:
            i = i + 1
        else:
            num = num // i
            if i not in res:
                res.append(i)
    res.append(num)
    return res

print (max(getPrimeFactors(600851475143)))