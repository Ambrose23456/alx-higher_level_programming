#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 65) and (ord(c) <= 90):
            print("{}".format(c), end ="")
        elif (ord(c) >= 97) and (ord(c) <= 122):
            print("{}".format(c) - 32)
            