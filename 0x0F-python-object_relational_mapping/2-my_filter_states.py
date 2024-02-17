#!/usr/bin/python3
""" 2-my_filter_states module"""
import MySQLdb
import sys


def filter_states():
    """
    Filter states based on the given state name.

    This function takes in the username, password, database
    name, and state name as command line arguments.
    It connects to a MySQL database using the provided credentials
    and retrieves all the states that match the given state name.
    The retrieved states are then printed to the console.

    Args:
        None

    Returns:
        None
    """
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(
            sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database_name)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}'" \
            " ORDER BY id ASC".format(state_name)
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))


if __name__ == "__main__":
    filter_states()
