#!/usr/bin/python3
def element_at(my_list, idx):
    my_list_len = len(my_list) - 1
    if idx < 0 or idx > my_list_len:
        return (None)
    else:
        return (my_list[idx])
