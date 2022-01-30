#!/usr/bin/python3
"""defining add integer"""

def add_integer(a, b=98):
    """this function is used to check if parameters are 
       integers or floats. After that it changes the 
       parameter into integer and adds them. 

       Args: 
           a(int): integer to be added
           b(int): integer to be added
       Returns:
           sum of a and b
    """
    if not((type(b) is int) or (type(b) is float)):
        raise TypeError("b must be an integer")
    elif not((type(a) is int) or (type(a) is float)):
        raise TypeError("a must be an integer")
    else:
        return int(a) + int(b)
    

