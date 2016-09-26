from back_end_requests import cinema


def fetch_all_from_db():
    from db.insert import InsertDB
    from db.declarative_db import Base, Movie

    session = InsertDB()
    movie_list = session.session.query(Movie)
    final_movie_dict = {}
    for movie in movie_list:
        print(movie.host_cinema_name, movie.name, movie.imdb_rating)
        if movie.host_cinema_name not in final_movie_dict.keys():

            final_movie_dict[movie.host_cinema_name] = [cinema.Movie(movie.name, movie.imdb_rating)]
        else:
            final_movie_dict[movie.host_cinema_name].append(cinema.Movie(movie.name, movie.imdb_rating))
    print(final_movie_dict)

    final_cinema_list = []
    for location in final_movie_dict.keys():
        final_cinema_list.append(cinema.Cinema(location, final_movie_dict[location]))
    print()
    print("Final Cinema List:")
    for item in final_cinema_list:
        print(item.name, item.listings)
    return final_cinema_list
