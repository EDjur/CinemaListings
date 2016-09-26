from flask import Flask, render_template
import os
from main import run_application, create_movie_list, update_db

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
PORT = int(os.getenv('VCAP_APP_PORT', 8080))
HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))


def setup_db():
    movie_list = create_movie_list()
    update_db(movie_list)


@app.route('/')
def hello_world():
    movie_list = run_application()
    return render_template('index.html', movie_list=movie_list)

if __name__ == '__main__':
    setup_db()
    app.run(host=HOST, port=PORT)
