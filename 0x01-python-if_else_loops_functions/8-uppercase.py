#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if ord(char) in range(97, 123):
            upper += chr(ord(char) - 32)
        else:
            upper += char
    print("{}".format(upper))
