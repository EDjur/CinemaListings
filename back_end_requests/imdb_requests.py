import json
import os

import requests
from imdbpie import Imdb
from tqdm import tqdm

# Get API key from environment
api_key = os.environ.get("OMDB_KEY")
BASE_OMDB_URL = f"http://www.omdbapi.com/?apikey={api_key}&t="


def initialize_imdb_connection():
    """DEPRECATED"""
    imdb = Imdb(anonymize=True)  # to proxy requests
    return imdb


def title_rating_tuple_list(cinema_list):
    """DEPRECATED"""
    print("Making imdb requests...")
    imdb = initialize_imdb_connection()
    for cinema in tqdm(cinema_list):
        for movie in tqdm(cinema.listings):
            title_id = imdb.search_for_title(movie.name)[0]['imdb_id']
            try:
                imdb_movie = imdb.get_title_by_id(title_id)  # bottleneck
                movie.imdb_rating = imdb_movie.rating
            except BaseException:  # Consider fixing this...
                movie.imdb_rating = None

    return cinema_list


def omdb_api_client(cinema_list):
    for cinema in tqdm(cinema_list):
        for movie in tqdm(cinema.listings):
            omdb_name_format = "+".join(movie.name.split())
            while True:
                print("Making OMDB Request")
                try:
                    response = json.loads(requests.get(BASE_OMDB_URL + omdb_name_format).text)
                except requests.RequestException:
                    continue
                break
            imdb_rating = response.get('imdbRating', 'N/A')
            meta_rating = response.get('Metascore', 'N/A')
            try:
                movie.imdb_rating = float(imdb_rating)
            except ValueError:
                movie.imdb_rating = None

            try:
                movie.meta_rating = int(meta_rating)
            except ValueError:
                movie.meta_rating = None

    return cinema_list
