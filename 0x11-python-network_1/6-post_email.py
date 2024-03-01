#!/usr/bin/python3

"""
This script takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response.
"""

import sys
import requests


def main():
    """
    Main function of the script.
    This function takes the URL and email address as command line arguments,
    creates a dictionary with the email as the value for the "email" key,
    sends a POST request to the URL with the payload as data,
    and prints the body of the response.
    """
    # Get the URL and email address from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email as the value for the "email" key
    payload = {"email": email}

    # Send a POST request to the URL with the payload as data
    response = requests.post(url, data=payload)

    # Print the body of the response
    print(response.text)


if __name__ == "__main__":
    main()
