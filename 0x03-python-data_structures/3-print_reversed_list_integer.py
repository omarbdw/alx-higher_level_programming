#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_my_list = my_list.reverse()
    for member in my_list:
        print("{:d}".format(member))
