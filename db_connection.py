from back_end_requests import cinelist_requests
from back_end_requests import imdb_requests
from db import declarative_db, insert


def create_movie_list():
    response = cinelist_requests.make_request()
    tuple_list = imdb_requests.title_rating_tuple_list(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff if x.imdb_rating else None, cinema.listings))
    return movie_list


def update_db():
    declarative_db.init_db()
    movie_list = create_movie_list()

    for cinema in movie_list:
        session = insert.InsertDB()
        session.add_new_cinema(cinema.name, cinema.listings)
        for movie in cinema.listings:
            session.add_new_movie(movie.name, movie.imdb_rating, cinema.name)


def fetch_movie_list_from_db():
    from db.fetch import fetch_all_from_db
    result = fetch_all_from_db()
    return result


