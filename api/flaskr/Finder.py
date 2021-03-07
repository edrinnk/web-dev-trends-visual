import pandas as pd
import numpy as np
from .SourceDataPath import SourceDataPath

class Finder:
        
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Finder, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        # TODO assign raw (yearly) dataframes here
        # & assign key data sections here
        # rest will follow 'get_example_item()'
        pass

    # EXAMPLE: this example will mean on init, not all data has to be built, but also data wont be unnecessarily rebuilt
    def get_example_item(self, year):
        # IF 'self.example_item' already exists, return 'self.example_item'
        # ELSE 'self.example_item' = extract_example_item(), return 'self.example_item'
        # *** Maybe this isn't need cos the frontend could hold onto the data instead??? ***
        pass
