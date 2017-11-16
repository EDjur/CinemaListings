import datetime
import json

import requests
from bs4 import BeautifulSoup

from .cinemas_config import create_cinema_config
from .domain import Cinema, Movie

# API_REQUESTS: http://cinelist.co.uk/
BASE_URL = "http://api.cinelist.co.uk"
NOW_SHOWING_URL = "/get/times/cinema/"

EVERYMAN_URL = "https://www.everymancinema.com/kings-cross"


def make_cinelist_request():
    print("Making Cinelist requests...")
    cinema_cfg = create_cinema_config()
    response_list = []
    for cinema in cinema_cfg.cinemas['cinemas']:
        response = requests.get(BASE_URL + NOW_SHOWING_URL + cinema['id'])
        response = json.loads(response.content.decode("utf-8"))
        response_list.append(Cinema(cinema['name'], get_titles_at_cinema(response)))

    return response_list


def make_everyman_request():
    print("Making Everyman requests...")
    content = requests.get(EVERYMAN_URL).content
    soup = BeautifulSoup(content, "html.parser")
    all_listings = soup.find_all("li", {"class": "gridRow filmItem"})
    listings_today = []

    today = datetime.datetime.now().date().strftime("%Y-%m-%d")
    for item in all_listings:
        if today not in item.get("data-film-session"):
            continue
        listings_today.append(item.find("a", "filmItemTitleLink"))

    # TODO: Change hardcoded Everyman title
    response_list = [Cinema("Everyman King's Cross", [Movie(film.get_text()) for film in listings_today])]
    return response_list


def make_individual_response(response):
    return get_titles_at_cinema(response)


def get_titles_at_cinema(top_level_response):
    titles = []
    movie_list = []

    for listing in top_level_response['listings']:
        title = listing['title']
        if title not in titles:
            titles.append(listing['title'])
            movie_list.append(Movie(name=title))

    return movie_list
