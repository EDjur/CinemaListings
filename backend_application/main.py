from back_end_requests import cinelist_requests, imdb_requests


def create_movie_list():
    response = cinelist_requests.make_request()
    tuple_list = imdb_requests.title_rating_tuple_list(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff, cinema.listings))
    return movie_list


if __name__ == '__main__':
    movie_list = create_movie_list()
    print("\nResult")
    print(movie_list)
    filtered_movie_list = filter_movie_list(movie_list)
    print(filtered_movie_list)
  ##  print("FILTERED FOR > 7.0 IMDB RATING: {}".format(filtered_movie_list))
