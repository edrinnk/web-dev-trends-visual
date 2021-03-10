import os
from flask import Flask, json, Response
import time as time
from .Finder import Finder
import pandas as pd

def create_app(test_config=None):
    # CONFIGURE FLASK =>
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        DEBUG=True # TEST
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    print('')

    # DATA SETUP =>
    # TODO do an initial contact api call that triggers starting data setup???
    finder = Finder()

    # API =>
    @app.route('/time')
    def hello():
        current_time = time.time()
        print(current_time)
        return {'time': current_time}

    @app.route('/exampleJson')
    def example1():
        data = finder.get_raw_dataframe(2019)
        data = data['browser'].to_dict()
        # response = app.response_class
        response = Response(
            response = json.dumps(data),
            status = 200,
            mimetype = 'application/json'
        )
        return response

    return app
    