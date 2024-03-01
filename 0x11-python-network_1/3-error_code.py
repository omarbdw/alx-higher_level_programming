#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It manages urllib.error.HTTPError exceptions and prints
the error code followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def main():
    """
    Main function of the script.
    This function takes a URL as a command
    line argument and sends a request to the URL.
    If the request is successful, it prints the response body.
    If an HTTP error occurs, it prints the error code.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 3-error_code.py <URL>")
        return

    # Get the URL from command line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL and open the response
        with urllib.request.urlopen(url) as response:
            # Read the response body and decode it using utf-8
            body = response.read().decode('utf-8')
            # Print the response body
            print(body)
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
