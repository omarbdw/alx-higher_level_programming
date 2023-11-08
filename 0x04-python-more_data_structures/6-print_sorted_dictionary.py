#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDic={}
    sortedDic = a_dictionary
    sortedDic = sorted(sortedDic.items())
    for key, value in sortedDic:
        print("{}: {}".format(key, value))
