#!/usr/bin/python3
""" Module that contains the function from_json_string """


def from_json_string(my_str):
    """ Function that returns an object represented by a JSON string """
    import json
    return json.loads(my_str)
