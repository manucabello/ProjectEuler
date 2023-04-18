"""
Escribe un programa que pida al usuario un número entero positivo y luego calcule y muestre por pantalla el factorial
de ese número. El factorial de un número es el producto de todos los números enteros positivos desde 1 hasta ese número.

 Por ejemplo, el factorial de 5 es 1 x 2 x 3 x 4 x 5 = 120. Debes utilizar un loop y una función.
"""


"""
This function calculates the factorial of a given number.
-Args:
    num (int): The number to calculate its factorial.
-Returns:
    int: The factorial of the given number.
"""
def factorial(num):
    res = 1
    i = 1
    while i <= num:
        res = res * i
        i = i + 1
    return res

num = int(input("Introduce el número al que calcular el factorial: "))
print(factorial(num))