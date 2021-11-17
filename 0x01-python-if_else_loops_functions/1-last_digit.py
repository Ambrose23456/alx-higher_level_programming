#!/usr/bin/python3
import random
number = random.randint(-10, 10)
lastDigit = number % 10
if (number > 5):
    print("Last digit of " + "number" + " is " + "lastDigit " + "and is greater than 5")
elif (number == 0):
    ("Last digit of " + "number" + " is " + "lastDigit " + "and is 0")
elif (number < 6) and (number != 0):
    ("Last digit of " + "number" + " is " + "lastDigit " + "and is less than 6 and not 0")
    
