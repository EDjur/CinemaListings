from imdbpie import Imdb


def initialize_imdb_connection():
    imdb = Imdb(anonymize=True)  # to proxy requests
    return imdb


def title_rating_tuple_list(cinema_list):
    imdb = initialize_imdb_connection()
    for cinema in cinema_list:
        print("Now fetching results for: {}, {}".format(cinema.name, cinema.listings))
        for movie in cinema.listings:
            title_id = imdb.search_for_title(movie.name)[0]['imdb_id']
            try:
                imdb_movie = imdb.get_title_by_id(title_id)  # bottleneck
                movie.imdb_rating = imdb_movie.rating
            except BaseException:
                movie.imdb_rating = None

    return cinema_list


