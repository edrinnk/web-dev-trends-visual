import pandas as pd
import numpy as np
from .DataCleaner import DataCleaner

class DataSectionExtractor:

    _singleton = None # TODO if this is only used x1 then no need for singleton!!!

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(DataSectionExtractor, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        pass

    # TODO change all to @staticmethod
    
    # tools
    def get_tools_dataframe(self, df):
        tools_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.tools)
        tools_dataframe = pd.DataFrame(list(tools_series))

        extract_experience_value = lambda item: item.get('experience') if type(item) is dict else item
        for column in list(tools_dataframe.columns):
            tools_dataframe[column] = tools_dataframe[column].apply(extract_experience_value)

        tools_dataframe = DataCleaner.clear_nan_from_dataframe(tools_dataframe) # INFO still required because inner object's values can contain NaNs
        return tools_dataframe

    # opinions
    def get_opinions_dataframe(self, df):
        opinions_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.opinions)

        opinions_dataframe = pd.DataFrame(list(opinions_series))
        opinions_dataframe = DataCleaner.clear_nan_from_dataframe(opinions_dataframe)

        return opinions_dataframe

    # years
    def get_years_of_experience(self, df):
        # INFO known unique options: ['2_5', '10_20', '1_2', '5_10', 'less_than_1', 'more_than_20']
        user_info_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.user_info)
        user_info_dataframe = pd.DataFrame(list(user_info_series))

        years_of_experience_series = user_info_dataframe.years_of_experience
        years_of_experience_list = [i for i in years_of_experience_series if type(i) == str]
        return years_of_experience_list

    # happiness
    def get_happiness_dataframe(self, df):
        happiness_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.happiness)

        happiness_dataframe = pd.DataFrame(list(happiness_series))
        happiness_dataframe = DataCleaner.clear_nan_from_dataframe(happiness_dataframe)

        for column in list(happiness_dataframe.columns):
            happiness_dataframe[column] = happiness_dataframe[column].apply(lambda value: int(value))
        return happiness_dataframe

    # text editors
    def get_text_editors(self, df):
        other_tools_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.other_tools)
        other_tools_dataframe = pd.DataFrame(list(other_tools_series))

        raw_series = DataCleaner.clear_nan_from_series(other_tools_dataframe.text_editors)
        raw_list = list(raw_series)

        text_editors_list = [item.get('choices') for item in raw_list if type(item) is dict]
        text_editors_list = [item[0] for item in text_editors_list if type(item) is list and len(item) > 0]
        return text_editors_list

    # countries
    def get_countries(self, df):
        user_info_series = DataCleaner.clear_nan_and_unequal_dictionaries_from_series(df.user_info)
        user_info_dataframe = pd.DataFrame(list(user_info_series))

        countries_series = DataCleaner.clear_nan_from_series(user_info_dataframe.country)
        return list(countries_series)
