#!/usr/bin/python3
"""
This script sends a POST request to
http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys


def main():
    """
    Main function of the script.
    """
    # Check if a command-line argument is provided
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    # Send a POST request to the specified URL with the letter as a parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        # Parse the response as JSON
        data = response.json()
        if data:
            # Print the id and name if data is not empty
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            # Print "No result" if data is empty
            print("No result")
    except ValueError:
        # Print "Not a valid JSON" if the response cannot be parsed as JSON
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
