#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    repeated = []
    for item in my_list:
        if item not in repeated:
            sum += item
            repeated.append(item)
    return (sum)
