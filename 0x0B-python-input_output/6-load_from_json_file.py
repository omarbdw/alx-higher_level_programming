#!/usr/bin/python3
""" Module that contains the function load_from_json_file """


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file """
    import json
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
