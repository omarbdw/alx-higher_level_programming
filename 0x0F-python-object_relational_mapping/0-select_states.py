#!/usr/bin/python3
""" 0-select_states module"""
import MySQLdb
import sys

def select_states():
	"""
	Connects to a MySQL server and selects all rows from the 'states' table.
	Prints the results.
	"""
	# Connect to MySQL server
	db = MySQLdb.connect(host="localhost", port=3306,
						 user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	# Create a cursor object
	cursor = db.cursor()

	# Execute the query
	cursor.execute("SELECT * FROM states ORDER BY id ASC")

	# Fetch all the rows
	rows = cursor.fetchall()

	# Print the results
	for row in rows:
		print(row)

	# Close the cursor and database connection
	cursor.close()
	db.close()

if __name__ == "__main__":
	select_states()
