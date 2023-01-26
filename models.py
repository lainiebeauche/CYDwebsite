from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """Represents a user in the database."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
