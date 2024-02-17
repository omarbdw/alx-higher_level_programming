#!/usr/bin/python3
""" 1-filter_states module"""
import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to a MySQL server and filters states whose name starts with 'N'.

    Args:
            username (str): The username for the MySQL server.
            password (str): The password for the MySQL server.
            database (str): The name of the database to connect to.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the filter_states function
    filter_states(username, password, database)
