import json

import requests

from .cinemas_config import create_cinema_config
from .domain import Cinema, Movie

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

    for listing in top_level_response['listings']:
        title = listing['title']
        if title not in titles:
            titles.add(listing['title'])
            movie_list.append(Movie(name=title))

    return movie_list

