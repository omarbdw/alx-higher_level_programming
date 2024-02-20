#!/usr/bin/python3
""" model_state.py - State class represents a state in the database. """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
            id (int): The unique identifier of the state.
            name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# Connect to MySQL server running on localhost at port 3306
engine = create_engine('mysql://localhost:3306')

# Import all classes that inherit from Base
# ...

# Create all tables in the database
Base.metadata.create_all(engine)
