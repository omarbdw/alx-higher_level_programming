#!/usr/bin/python3
""" 8-model_state_fetch_first.py - Fetches
the first State object from the database.

Usage:

    $ ./8-model_state_fetch_first.py <mysql-username> <mysql-password> <database-name>

Example:
    
        $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
        1: California

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database
    # name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if the table is empty
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
