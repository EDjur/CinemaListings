
from back_end_requests import imdb_requests
from back_end_requests import cinelist_requests


def create_movie_list():
    response = cinelist_requests.make_request()
    tuple_list = imdb_requests.title_rating_tuple_list(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff if x.imdb_rating else None, cinema.listings))
    return movie_list


def update_db(movie_list):
    from db import declarative_db, insert
    declarative_db.init_db()

    for cinema in movie_list:
        session = insert.InsertDB()
        session.add_new_cinema(cinema.name, cinema.listings)
        for movie in cinema.listings:
            session.add_new_movie(movie.name, movie.imdb_rating, cinema.name)


def fetch_movie_list_from_db():
    from db.insert import InsertDB
    from db.declarative_db import Cinema, Base, Movie
    session = InsertDB()
    movie_list = session.session.query(Movie)
    final_movie_list = []
    for movie in movie_list:
        print(movie.host_cinema_name, movie.name, movie.imdb_rating)
        if movie.host_cinema_name in final_movie_list:
            final_movie_list




def run_application():
    movie_list = create_movie_list()
    print(movie_list)
    update_db(movie_list)
    fetch_movie_list_from_db()
    return filter_movie_list(movie_list, 7)

if __name__ == '__main__':
    run_application()

