#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


def main():
    """
    Main function to fetch and print the response from the URL
    """
    # Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Open the URL and read the response
    with urllib.request.urlopen(url) as response:
        # Read the response body
        body = response.read()

        # Print the response details
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
