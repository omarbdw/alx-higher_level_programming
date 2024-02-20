#!/usr/bin/python3
""" 9-model_state_filter_a.py - Lists all State objects that contain the letter a from the database hbtn_0e_6_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
