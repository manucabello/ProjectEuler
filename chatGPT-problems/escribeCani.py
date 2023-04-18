"""
Escribe una función en Python que reciba una cadena de caracteres y devuelva una nueva cadena donde todas las letras
en posiciones impares se conviertan en mayúsculas y las letras en posiciones pares se mantengan en minúsculas.

La posición de la primera letra es 0.

Por ejemplo, si la cadena de entrada es "ejemplo", la salida debería ser "eJeMpLo".
"""


"""
Writes a string where every other character is capitalized and the rest are in lowercase.
- Args:
    cadena (str): the string to be converted to Cani-style text.
- Returns:
    res (str): the Cani-style text resulting from the conversion.
"""
def escribeCani(cadena):
    res = ""
    i = 0
    while i < len(cadena):
        if i % 2 == 0:
            res = res + cadena[i].lower()
        else:
            res = res + cadena[i].upper()
        i = i + 1
    return res


print(escribeCani("ejemplo"))
