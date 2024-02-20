#!/usr/bin/python3
""" 5-filter_cities.py - Retrieves a list of cities in a given state from a MySQL database. """
import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Retrieves cities from a MySQL database based on a given state name.

    Args:
            username (str): The username for the MySQL server.
            password (str): The password for the MySQL server.
            database (str): The name of the MySQL database.
            state_name (str): The name of the state to filter cities by.

    Returns:
            None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute(
        "SELECT cities.name FROM cities JOIN states ON cities.state_id \
                = states.id WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name,)
    )

    # Fetch all the rows
    rows = cursor.fetchall()

    # Create a list of cities
    cities = [row[0] for row in rows]

    # Print the cities in the desired format
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the filter_cities function
    filter_cities(username, password, database, state_name)
