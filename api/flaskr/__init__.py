import os
from flask import Flask
import time as time
from .DataCleaner import DataCleaner
from .SourceDataPath import SourceDataPath

def create_app(test_config=None):
    # CONFIGURE FLASK =>
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    # IGNORE =>
    print('')

    # API =>
    @app.route('/time')
    def hello():
        current_time = time.time()
        print(current_time)
        return {'time': current_time}

    # DATA-SET SETUP =>


    # TESTING STUFF =>
    print('@TESTING EXTERNAL MODULE: ' + SourceDataPath.get_2016())

    return app