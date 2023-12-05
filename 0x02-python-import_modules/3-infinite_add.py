#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        adds = 0

        for i in range(1, len(argv)):
            adds += int(argv[i])

        print("{}".format(adds))
    else:
        print(0)
