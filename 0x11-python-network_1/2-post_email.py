#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email
as a parameter and displays the response body.
"""

import urllib.parse
import urllib.request
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with
    the given email as a parameter.
    Prints the response body.
    """
    # Encode the email parameter and convert it to bytes
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request with the URL, data, and method
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and get the response
    with urllib.request.urlopen(req) as response:
        # Read the response body and decode it to a string
        body = response.read().decode('utf-8')
        # Print the response body
        print(body)


if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
