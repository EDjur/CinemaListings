from imdbpie import Imdb
from tqdm import tqdm


def initialize_imdb_connection():
    imdb = Imdb(anonymize=True)  # to proxy requests
    return imdb


def title_rating_tuple_list(cinema_list):
    print("Making imdb requests...")
    imdb = initialize_imdb_connection()
    for cinema in tqdm(cinema_list):
        for movie in tqdm(cinema.listings):
            title_id = imdb.search_for_title(movie.name)[0]['imdb_id']
            try:
                imdb_movie = imdb.get_title_by_id(title_id)  # bottleneck
                movie.imdb_rating = imdb_movie.rating
            except BaseException: # Consider fixing this...
                movie.imdb_rating = None

    return cinema_list


