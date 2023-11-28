#!/usr/bin/python3
for get_value in range(0, 100):
    if get_value == 99:
        print("{value}".format(value=get_value))
    else:
        print("{value},".format(value=get_value).zfill(3), end=' ')
