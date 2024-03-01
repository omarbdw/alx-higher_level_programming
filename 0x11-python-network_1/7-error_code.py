#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints: Error code: followed by the value of the HTTP status code.
"""

import sys
import requests


def main():
    """
    Main function of the script.
    This function sends a GET request to the
    specified URL and checks the response status code.
    If the status code is greater than or equal
    to 400, it prints the error code.
    Otherwise, it prints the response body.
    """
    # Get the URL from command line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        # Print the error code
        print("Error code:", response.status_code)
    else:
        # Print the response body
        print(response.text)


if __name__ == "__main__":
    main()
