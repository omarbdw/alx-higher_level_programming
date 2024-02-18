#!/usr/bin/python3
import MySQLdb
import sys


def get_cities_by_state(username, password, database):
    """
    Retrieves a list of cities along with their
    corresponding state names from a MySQL database.

    Args:
            username (str): The username for the MySQL server.
            password (str): The password for the MySQL server.
            database (str): The name of the database to connect to.

    Returns:
            list: A list of tuples containing the city ID,
            city name, and state name.

    Raises:
            MySQLdb.Error: If there is an error
            executing the SQL query or connecting to the database.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query
        cursor.execute(
                "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        return rows
    except MySQLdb.Error as e:
        print("An error occurred:", e)
        raise
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Retrieve cities by state
    cities = get_cities_by_state(username, password, database)

    # Display the results
    for city in cities:
        print(city)
