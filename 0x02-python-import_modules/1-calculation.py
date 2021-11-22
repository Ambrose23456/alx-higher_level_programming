#!/usr/bin/python3
"""performs add, subtract, divide and multiplication on given numbers"""
from calculator_1 import sub, mul, div, add 
a = 10
b = 5

print("{} + {} = {}".format(a,b, add(a,b)))

print("{} - {} = {}".format(a,b, sub(a,b)))

print("{} * {} = {}".format(a,b, mul(a,b)))

print("{} / {} = {}".format(a,b, div(a,b)))
