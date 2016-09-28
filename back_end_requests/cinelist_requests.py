import json

import requests

from .cinema import Cinema, Movie
from .cinemas_config import create_cinema_config

# API_REQUESTS: http://cinelist.co.uk/
BASE_URL = "http://api.cinelist.co.uk"
NOW_SHOWING_URL = "/get/times/cinema/"


def make_request():
    print("Making Cinelist requests...")
    cinema_cfg = create_cinema_config()
    response_list = []
    for cinema in cinema_cfg.cinemas['cinemas']:
        response = requests.get(BASE_URL + NOW_SHOWING_URL + cinema['id'])
        response = json.loads(response.content.decode("utf-8"))
        response_list.append(Cinema(cinema['name'], get_titles_at_cinema(response)))

    return response_list


def make_individual_response(response):
    return get_titles_at_cinema(response)


def get_titles_at_cinema(top_level_response):
    titles = set()
    movie_list = []

    # TODO: Make this nicer i.e. avoid double for-loop
    for listing in top_level_response['listings']:
        titles.add(listing['title'])

    for title in titles:
        movie_list.append(Movie(name=title))

    return movie_list

