#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list
    for element in my_list:
        if element == search:
            element = replace
