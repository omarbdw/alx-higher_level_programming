#!/usr/bin/python3
import sys
if __name__ == "__main__":

    len = len(sys.argv) - 1
    if len == 0:
        print("0 arguments.")
    if len == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if len > 1:
        print("{:d} arguments:".format(len))
        c = 0
        for i in sys.argv[1:len+1]:
            c += 1
            print("{}: {}".format(c, i))
