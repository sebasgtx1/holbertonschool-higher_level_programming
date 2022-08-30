#!/usr/bin/python3
"""
Contains State class that inherits from Base (declarative_base())
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class that defines an state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
