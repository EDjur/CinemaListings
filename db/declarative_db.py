import os
from pathlib import Path
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


def init_db():

    # Create an engine that stores data in the local directory's
    # sqlalchemy.db file.
    print('sqlite:///' + str(Path(__file__).parents[1]) + os.sep + "db" + os.sep + "sqlalchemy.db")
    engine = create_engine('sqlite:///' + str(Path(__file__).parents[1]) + os.sep + "db" + os.sep + "sqlalchemy.db")

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)


class Cinema(Base):
    __tablename__ = 'cinema'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    listings = Column(String(250))


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    imdb_rating = Column(Float)
    host_cinema_name = Column(String(250), ForeignKey('cinema.name'))
    host_cinema = relationship(Cinema)



