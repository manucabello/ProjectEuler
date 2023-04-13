#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


"""
Method to get the prime factors of a number using successive division method
- Args:
    param1: The number from which to obtain the prime factors
- Returns:
    res: The list of prime factors of param1
"""
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

# Print max value of the list with the prime factors of 600851475143
print (max(getPrimeFactors(600851475143)))