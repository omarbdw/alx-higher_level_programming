#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for n in my_list:
        if (n % 2) == 0:
            newList.append(True)
        else:
            newList.append(False)
    return (newList)
