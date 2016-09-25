from imdbpie import Imdb


def initialize_imdb_connection():
    imdb = Imdb(anonymize=True)  # to proxy requests
    return imdb


def title_rating_tuple_list(cinema_list):
    imdb = initialize_imdb_connection()
    for cinema in cinema_list:
        print("Now fetching results for: {}, {}".format(cinema.name, cinema.listings))
        for movie in cinema.listings:
            print(movie)
            title_id = imdb.search_for_title(movie.name)[0]['imdb_id']
            imdb_movie = imdb.get_title_by_id(title_id)  # bottleneck
            print(imdb_movie.rating)
            movie.imdb_rating = imdb_movie.rating

    return cinema_list


