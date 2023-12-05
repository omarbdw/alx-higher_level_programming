#!/usr/bin/python3
""" Module that contains the function load_from_json_file """
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]
my_list = []
if os.path.exists("./add_item.json"):
    my_list = load_from_json_file(filename)
save_to_json_file((my_list + args), filename)
