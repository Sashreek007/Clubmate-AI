from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    JSON,
    ForeignKey,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

""" sqlalchemy is a python library that makes it easier to work with databases. It is called an Object Relational Mapper(orm)"""

# this creates a base class that the orm models i.e the  python classes that map to database tables inherit from
Base = declarative_base()


class Club(Base):
    __tablename__ = "clubs"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    discord_server_id = Column(String(75))

    members = relationship("Member", back_populates="club")
    events = relationship("Event", back_populates="club")


class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    club_id = Column(
        Integer, ForeignKey("clubs.id")
    )  # this creates a reference to the clubs tables

    discord_user_id = Column(String, nullable=False)

    role = Column(String, default="member")  # role of the discord user
    joined_at = Column(DateTime)

    club = relationship("Club", back_populates="members")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)

    club_id = Column(Integer, ForeignKey("clubs.id"))

    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    location = Column(String)
    created_by = Column(Integer, ForeignKey("members.id"))

    club = relationship("Club", back_populates="events")

    creator = relationship("Member")
