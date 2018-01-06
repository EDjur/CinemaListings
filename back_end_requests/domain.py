class Cinema:
    def __init__(self, name=None, listings=None):
        self.name = name
        self.listings = listings  # List of Movie objects


class Movie:
    def __init__(self, name=None, imdb_rating=None, meta_rating=None):
        self.name = name
        self.imdb_rating = imdb_rating
        self.meta_rating = meta_rating
