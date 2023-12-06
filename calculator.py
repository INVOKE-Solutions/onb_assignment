"""
This script function to calculate numerical values that performs
addition, substraction, division and multiplication
This function accepts user input ie the 2 numerical values
and return the result value
"""
 
# perform the addition function
def addition(value_1: float,value_2 : float):
    """
    Function will return result of addition from 
    parameters when value_1 + value_2
    
    Params:
    - value_1 (float): The first number for addition operation.
    - value_2 (float): The first number for addition operation.
    Example:
    addition (1,4)
    = 5.0
    """
    return value_1 + value_2

# perform the subtraction function
def substraction(value_1: float,value_2 : float):
    """
    Function will return result of subtraction from 
    parameters when value_1 - value_2
    
    Params:
    - value_1 (float): The first number for subtraction operation.
    - value_2 (float): The first number for subtraction operation.
    Example:
    substraction (1,4)
    = -3.0
    """
    return value_1 - value_2

# perform the multiplication function
def multiplication(value_1: float,value_2 : float):
    """
    Function will return result of multiplication from 
    parameters when value_1 + value_2
    
    Params:
    - value_1 (float): The first number for multiplication operation.
    - value_2 (float): The first number for multiplication operation.
    Example:
    multiplication (1,4)
    = 4.0
    """
    return value_1 * value_2

# perform the division function
def division(value_1: float,value_2 : float):
    """
    Function will return result of division from 
    parameters when value_1 + value_2
    
    Params:
    - value_1 (float): The first number for division operation.
    - value_2 (float): The first number for division operation.
    Example:
    division (1,4)
    = 0.25
    """
    return round((value_1 / value_2),3)