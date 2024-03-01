#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def main():
    """
    Main function of the script.
    Retrieves the value of the X-Request-Id
    header from a given URL and prints it.
    """
    # Get the URL from the command line argument
    url = sys.argv[1]

    # Create a request object with the given URL
    req = urllib.request.Request(url)

    # Send the request and get the response
    with urllib.request.urlopen(req) as response:
        # Get the headers from the response
        headers = response.headers

        # Get the value of the X-Request-Id header
        x_request_id = headers.get('X-Request-Id')

        # Print the value of the X-Request-Id header
        print(x_request_id)


if __name__ == "__main__":
    main()
