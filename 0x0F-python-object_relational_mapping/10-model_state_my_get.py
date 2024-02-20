#!/usr/bin/python3
""" 10-model_state_my_get.py - Retrieves the ID of the State object with the given name from the database hbtn_0e_6_usa. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_id(mysql_username, mysql_password, database_name, state_name):
    """
    Function that retrieves the ID of the State object with the given name
    from the database hbtn_0e_6_usa.

    Args:
            mysql_username (str): MySQL username.
            mysql_password (str): MySQL password.
            database_name (str): Name of the database.
            state_name (str): Name of the state.

    Returns:
            int: ID of the State object if found, otherwise -1.
    """
    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}\
        @localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state name
    state = session.query(State).filter(State.name == state_name).first()

    # Return the result
    if state:
        return state.id
    else:
        return -1


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Get the state ID
    state_id = get_state_id(
        mysql_username, mysql_password, database_name, state_name)

    # Print the result
    if state_id != -1:
        print(state_id)
    else:
        print("Not found")
