from back_end_requests import web_requests
from back_end_requests import imdb_requests
from db import declarative_db, insert
from tqdm import tqdm


def create_movie_list():
    print("Creating movie list...")
    response = web_requests.make_cinelist_request()
    response.extend(web_requests.make_everyman_request())
    tuple_list = imdb_requests.omdb_api_client(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff if x.imdb_rating else None, cinema.listings))
    return movie_list


def update_db():
    print("UPDATING DATABASE")
    declarative_db.init_db()
    movie_list = create_movie_list()

    print("Inserting movie data into database...")
    for cinema in tqdm(movie_list):
        session = insert.InsertDB()
        session.add_new_cinema(cinema.name, cinema.listings)
        for movie in cinema.listings:
            session.add_new_movie(movie.name, movie.imdb_rating, cinema.name)
    print("DONE UPDATING DATABASE")


def fetch_movie_list_from_db():
    from db.fetch import fetch_all_from_db
    result = fetch_all_from_db()
    return result


