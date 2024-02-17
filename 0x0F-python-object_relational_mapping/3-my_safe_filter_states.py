#!/usr/bin/python3
""" 3-safe_filter_states module"""
import MySQLdb
import sys


def safe_filter_states():
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

    Raises:
            MySQLdb.Error: If there is an error connecting to
            the MySQL database or executing the query.
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
        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))


if __name__ == "__main__":
    safe_filter_states()
