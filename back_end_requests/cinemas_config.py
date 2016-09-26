import os
import json
from pathlib import Path


class CinemasConfig:
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(path):
            raise FileNotFoundError("Error: Missing cinemas_full.json file in {}".format(path))
        with open(path, encoding="utf-8") as cinemas_json:
            self.cinemas = json.load(cinemas_json)


cinema_config = None


def create_cinema_config(path=None):
    if not path:
        path = str(Path(__file__).parents[1]) + os.sep + "cinemas_example.json"
    global cinema_config
    if not cinema_config:
        cinema_config = CinemasConfig(path)
        return cinema_config
    else:
        path = cinema_config.path
        cinema_config = CinemasConfig(path)
        return cinema_config
