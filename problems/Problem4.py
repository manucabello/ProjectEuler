#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


"""
Method to get the palindrome numbers made from the product of two 3-digit numbers.
- Args:
    None
- Returns:
    res: The list of palindrome numbers made from the product of two 3-digit numbers.
"""
def getPalindromeNumbers():
    res = []
    i = 100
    while i < 1000:
        j = 100
        while j < 1000:
            aux = i * j
            if isPalindrome(aux):
                res.append(aux)
            j = j + 1
        i = i + 1
    return res


"""
Method to get the reverse of a number
- Args:
    param1: Number to reverse
- Returns:
    res: The reversed number
"""
def reverseNumber(num):
    res = 0
    while num > 0:
        res = res * 10 + (num % 10)
        num //= 10
    return res


"""
Method to check if a number is palindrome
- Args:
    param1: The number to check
- Returns:
    True if the number is palindrome
    False if the number is not palindrome
"""
def isPalindrome(num):
    return reverseNumber(num) == num


# Print the max palindrome number made from the product of two 3-digit numbers.
print (max(getPalindromeNumbers()))