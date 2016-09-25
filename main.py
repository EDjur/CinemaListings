from pathlib import Path

from back_end_requests import imdb_requests
from jinja2 import Environment, FileSystemLoader

from back_end_requests import cinelist_requests


def create_movie_list():
    response = cinelist_requests.make_request()
    tuple_list = imdb_requests.title_rating_tuple_list(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff if x.imdb_rating else None, cinema.listings))
    return movie_list


def run_application():
    movie_list = create_movie_list()
    return filter_movie_list(movie_list, 7)

if __name__ == '__main__':
    run_application()

