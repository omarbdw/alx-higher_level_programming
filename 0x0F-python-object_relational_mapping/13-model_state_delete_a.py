#!/usr/bin/python3
""" 13-model_state_delete_a.py - Deletes State objects with names containing 'a' from the database. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    This script deletes State objects with names
    containing 'a' from the database.
    It requires three command line arguments:
    username, password, and db_name.
    """

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete State objects with name containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit the changes
    session.commit()
