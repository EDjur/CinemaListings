from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.declarative_db import Cinema, Base, Movie
from pathlib import Path
import os


class InsertDB:
    def __init__(self):
        self.engine = create_engine('sqlite:///' + str(Path(__file__).parents[1]) + os.sep + "db" + os.sep + "sqlalchemy.db")
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = self.engine

        self.DBSession = sessionmaker(bind=self.engine)
        # A DBSession() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object. Any change made against the objects in the
        # session won't be persisted into the database until you call
        # session.commit(). If you're not happy about the changes, you can
        # revert all of them back to the last commit by calling
        # session.rollback()
        self.session = self.DBSession()

    def add_new_cinema(self, name=None, listings=None):
        listings_string = ', '.join([movie.name for movie in listings])
        print(listings_string)
        self.new_cinema = Cinema(name=name, listings=listings_string) # Used to connect the movies to a cinema
        row = self.session.query(Cinema).filter(Cinema.name == name).all()
        if row:
            row[0].name = name
            row[0].listings = listings_string
            print("Cinema already exists. Merging entries...")
        else:
            self.session.add(self.new_cinema)
        self.session.commit()

    def add_new_movie(self, name=None, imdb_rating=None, host_cinema_name=None):
        # session = init_db()
        new_movie = Movie(name=name, imdb_rating=imdb_rating, host_cinema=self.new_cinema)
        row = self.session.query(Movie).filter(Movie.name == name and Movie.host_cinema == host_cinema_name).all()
        if row:
            row[0].name = name
            print("Movie already exists at this cinema ({}) already exists. Merging entries...".format(host_cinema_name))
        else:
            self.session.add(new_movie)
        self.session.commit()
