#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL, and
displays the value of the variable X-Request-Id
in the response header.
"""

import requests
import sys


def main():
    """
    Main function of the script.
    """
    # Get the URL from command line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of the 'X-Request-Id' header from the response
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value of 'X-Request-Id'
    print(x_request_id)


if __name__ == "__main__":
    main()
