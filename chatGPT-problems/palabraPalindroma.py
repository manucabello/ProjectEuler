#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Escribe un programa que solicite al usuario ingresar una cadena de texto y luego determine si esa cadena es un
palíndromo o no. Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás que de atrás hacia
adelante.

Por ejemplo, las palabras "radar" y "reconocer" son palíndromos, al igual que la frase "anita lava la tina".

El programa debe imprimir en pantalla si la cadena ingresada es un palíndromo o no.
"""


"""
Method to check if a word is palindrome
- Args:
    param1: The word to check
- Returns:
    True if the word is palindrome
    False if the word is not palindrome
"""
def isWordPalindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    return word == word[::-1]

word = input("Escribe una palabra para comprobar si es palíndroma: ")
print (isWordPalindrome(word))