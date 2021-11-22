#!/usr/bin/python3
"""prints the number and list of arguments passed"""
if __name__ = "main":
    import sys
    i = len(sys.argv) - 1

if len == 0:
    print("{} arugument.".format(i))
elif len == 1:
    print("{} argument:".format(i))
elif len > 1:
    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{} : {}".format(i, arg))
        i += 1
