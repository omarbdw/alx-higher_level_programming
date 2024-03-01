#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status
"""

import requests


def main():
    """
    Main function
    """
    # Send a GET request to the specified URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Print the response details
    print("Body response:")
    # Print the type of the response text
    print("\t- type: {}".format(type(response.text)))
    # Print the content of the response text
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
