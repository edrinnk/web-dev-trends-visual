# ensure paths cannot be edited by use functions instead of variables
class SourceDataPath:
    
    @staticmethod
    def get_2016():
        return 'flaskr\\source_data\\state_of_js_2016_normalized_responses_anon.ndjson'

    @staticmethod
    def get_2017():
        return 'flaskr\\source_data\\state_of_js_2017_normalized_responses_anon.ndjson'

    @staticmethod
    def get_2018():
        return 'flaskr\\source_data\\state_of_js_2018_normalized_responses_anon.ndjson'

    @staticmethod
    def get_2019():
        return 'flaskr\\source_data\\state_of_js_2019_normalized_responses_anon.ndjson'
