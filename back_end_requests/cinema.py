class Cinema:
    def __init__(self, name=None, listings=None):
        self.name = name
        self.listings = listings  # List of Movie objects

    #def __repr__(self):
    #    return "{}: {}".format(self.name, self.listings)


class Movie:
    def __init__(self, name=None, imdb_rating=None):
        self.name = name
        self.imdb_rating = imdb_rating

    #def __repr__(self):
     #   return "({}, {})".format(self.name, self.imdb_rating) if self.imdb_rating else "{}".format(self.name)
