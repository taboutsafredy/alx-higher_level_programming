#!/usr/bin/python3
out = ""
for char in range(97, 123):
    out += "{}".format(chr(char - 32) if (char % 2 != 0) else chr(char))
print("{}".format(out[::-1]), end="")
