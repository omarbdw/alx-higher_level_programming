#!/usr/bin/python3

"""
This script takes GitHub credentials (username and password)
and uses the GitHub API to display the user's id.
"""

import sys
import requests


def get_user_id(username, password):
    """
    Retrieves the user ID from the GitHub API
    using the provided username and password.

    Args:
        username (str): The GitHub username.
        password (str): The GitHub password.

    Returns:
        int: The user ID if found, None otherwise.
    """
    # Construct the URL for the GitHub API using the provided username
    url = f"https://api.github.com/users/{username}"

    # Send a GET request to the GitHub API with the provided credentials
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        # If the response is successful, extract the
        # user data from the JSON response
        user_data = response.json()

        # Get the user's id from the user data
        user_id = user_data.get("id")

        if user_id:
            # If the user id is found, return it
            return user_id
        else:
            # If the user id is not found, print an error message
            print("User ID not found.")
    else:
        # If there is an error accessing the GitHub API, print an error message
        print("Error accessing GitHub API.")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Get the username and password from the command line arguments
        username = sys.argv[1]
        password = sys.argv[2]

        # Call the get_user_id function with the provided credentials
        user_id = get_user_id(username, password)

        if user_id:
            # If the user id is found, print it
            print(f"User ID: {user_id}")
    else:
        # If the username and password are not provided
        # as arguments, print an error message
        print("Please provide username and password as arguments.")
