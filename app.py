import os

from flask import Flask, render_template

from db_connection import fetch_movie_list_from_db, update_db

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
PORT = int(os.getenv('VCAP_APP_PORT', 8080))
HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))


def setup_db():
    update_db()


def sort_by_imdb_rating(cinema_list):
    for cinema in cinema_list:
        cinema.listings.sort(key=lambda x: x.imdb_rating if x.imdb_rating else False, reverse=True)
    cinema_list.sort(key=lambda x: x.name)
    return cinema_list


@app.route('/')
def index():
    cinema_list = fetch_movie_list_from_db()
    cinema_list = sort_by_imdb_rating(cinema_list)
    # optionally filter movie list filter_movie_list(movie_list, 7)
    return render_template('index.html', movie_list=cinema_list)

if __name__ == '__main__':
    setup_db()
    app.run(host=HOST, port=PORT)
