#!/usr/bin/python3
""" Module that contains the function to_json_string """


def to_json_string(my_obj):
    """ Function that returns the JSON
    representation of an object (string) """
    import json
    return json.dumps(my_obj)
