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
        print('@Finder data assignment STARTED')
        self.initialize_raw_dataframes()
        print('@Finder data assignment DONE')

    def initialize_raw_dataframes(self):
        # self.raw_dataframes = {
        #     2016: pd.read_json(SourceDataPath.get_2016(), lines=True),
        #     2017: pd.read_json(SourceDataPath.get_2017(), lines=True),
        #     2018: pd.read_json(SourceDataPath.get_2018(), lines=True),
        #     2019: pd.read_json(SourceDataPath.get_2019(), lines=True)
        # }

        # FOR DEV ONLY =>
        rows_to_read = 100
        self.raw_dataframes = {
            2016: pd.read_json(SourceDataPath.get_2016(), lines=True, nrows=rows_to_read),
            2017: pd.read_json(SourceDataPath.get_2017(), lines=True, nrows=rows_to_read),
            2018: pd.read_json(SourceDataPath.get_2018(), lines=True, nrows=rows_to_read),
            2019: pd.read_json(SourceDataPath.get_2019(), lines=True, nrows=rows_to_read)
        }

    def get_raw_dataframe(self, year):
        return self.raw_dataframes[year]