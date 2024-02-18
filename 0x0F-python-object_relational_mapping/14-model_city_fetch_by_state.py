#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City


def fetch_cities_by_state(username, password, database):
    """
    Fetches and prints all City objects from the database sorted by cities.id.

    Args:
            username (str): MySQL username.
            password (str): MySQL password.
            database (str): Database name.
    """
    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects from the database and sort by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py \
            <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the fetch_cities_by_state function
    fetch_cities_by_state(username, password, database)
