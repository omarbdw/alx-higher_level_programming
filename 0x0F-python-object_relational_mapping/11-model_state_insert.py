#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state(username, password, database):
    """
    Insert a new state into the database.

    Args:
            username (str): The MySQL username.
            password (str): The MySQL password.
            database (str): The MySQL database name.
    """
    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to persist the changes to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)


if __name__ == "__main__":
    # Get the MySQL username, password, and database
    # name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    insert_state(username, password, database)
