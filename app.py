from flask import Flask, render_template
import os
from main import run_application

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


@app.route('/')
def hello_world():
    movie_list = run_application()
    return render_template('index.html', movie_list=movie_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port)
