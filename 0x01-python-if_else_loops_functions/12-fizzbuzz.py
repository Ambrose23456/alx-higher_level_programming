#!/usr/bin/python3
def fizzbuzz():
    """the famous fizzBuzz challenge. Here a range of numbers from 1 to 100 
       is printed and along the way at designated points "fizz", "Buzz" or 
        Fizzbuzz" is printed instead of the number in the sequence"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
