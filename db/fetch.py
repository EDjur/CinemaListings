from back_end_requests import domain


def fetch_all_from_db():
    from db.insert import InsertDB
    from db.declarative_db import Movie

    session = InsertDB()
    movie_list = session.session.query(Movie)
    final_movie_dict = {}
    for movie in movie_list:
        if movie.host_cinema_name not in final_movie_dict.keys():

            final_movie_dict[movie.host_cinema_name] = [domain.Movie(movie.name, movie.imdb_rating)]
        else:
            final_movie_dict[movie.host_cinema_name].append(domain.Movie(movie.name, movie.imdb_rating))

    final_cinema_list = []
    for location in final_movie_dict.keys():
        final_cinema_list.append(domain.Cinema(location, final_movie_dict[location]))

    return final_cinema_list
