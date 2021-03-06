import pandas as pd
import numpy as np

class DataCleaner:

    # remove any index (row) that has NaNs
    @staticmethod
    def clear_nan_from_dataframe(df):
        new = df.dropna(axis = 0)
        new.reset_index(inplace = True, drop = True)
        return new

    # remove any NaNs from a series
    @staticmethod
    def clear_nan_from_series(srs):
        new = srs.dropna()
        new.reset_index(inplace = True, drop = True)
        return new

    # remove dictionaries that don't have identical keys (this is required before converting to a dataframe)
    @staticmethod
    def clear_nan_and_unequal_dictionaries_from_series(srs, index_with_keys_to_match = 0):
        new_series = DataCleaner.clear_nan_from_series(srs)
        keys_to_match = list(new_series[index_with_keys_to_match].keys())
        new_series = pd.Series([item for item in new_series if list(item.keys()) == keys_to_match])
        return new_series

    # return a list of unique values in a list/series/array
    @staticmethod
    def get_unique_values(array_like):
        srs = array_like if type(array_like) is pd.Series else pd.Series(array_like)
        return list(srs.unique())
        