#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        fct(args)
        return(fct(args))
    except:
        print("Exception: ", file=sys.stderr)
