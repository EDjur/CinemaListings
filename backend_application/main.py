from backend_application.back_end_requests import cinelist_requests, imdb_requests
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def create_movie_list():
    response = cinelist_requests.make_request()
    tuple_list = imdb_requests.title_rating_tuple_list(response)
    return tuple_list


def filter_movie_list(movie_list, cutoff=7.5):
    for cinema in movie_list:
        cinema.listings = list(filter(lambda x: x.imdb_rating > cutoff, cinema.listings))
    return movie_list


def render_jinja_template(movie_list):

    path_to_static = str(Path(__file__).parents[1]) + "\static"
    path_to_templates = path_to_static + "\\templates"
    print(path_to_templates)
    env = Environment(loader=FileSystemLoader(path_to_templates))
    template = env.get_template('index.html')
    output_from_parsed_template = template.render(foo=movie_list)
    print(output_from_parsed_template)

    # to save the results
    with open(path_to_static + "\\index.html", "w") as fh:
        fh.write(output_from_parsed_template)


def run_application():
    movie_list = create_movie_list()
    filtered_movie_list = filter_movie_list(movie_list)
    render_jinja_template(filtered_movie_list)

if __name__ == '__main__':
    run_application()
  ##  print("FILTERED FOR > 7.0 IMDB RATING: {}".format(filtered_movie_list))
