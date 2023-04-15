"""
Escribe una función en Python que tome una lista de números enteros y devuelva el número más grande y el número más
pequeño de la lista. La función debe manejar el caso en que la lista esté vacía y devolver None para ambos valores en
ese caso.
"""

"""
This function takes a list of integers as input and returns a dictionary containing the largest and smallest
integers in the list.
Args:
    my_list (list): A list of integers.
Raises:
    ValueError: If the input list is empty.
Returns:
    dict: A dictionary containing the largest and smallest integers in the list.
"""
def getLargestAndSmallest(my_list):
    # Check if the input list is empty
    if not my_list:
        raise ValueError("The list is empty.")

    # Initialize the dictionary with the first element of the list
    res = {
        'largest': my_list[0],
        'smallest': my_list[0]
    }

    # Loop through the list and update the dictionary if a larger or smaller element is found
    for i in my_list:
        if i > res['largest']:
            res['largest'] = i
        if i < res['smallest']:
            res['smallest'] = i

    # Return the resulting dictionary
    return res

print (getLargestAndSmallest([6,1,7,2,3,1,9]))