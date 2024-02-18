#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, db_name):
    """
    Update the name of a state with id 2 in the database.

    Args:
            username (str): The username for the database connection.
            password (str): The password for the database connection.
            db_name (str): The name of the database.
    """
    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update state name
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    update_state_name(username, password, db_name)
