from flask import Flask
import time
import sys
import json
import pandas as pd
import numpy as np
import math

app = Flask(__name__)

# test
@app.route('/time')
def get_current_time():
    print(time.time(), file=sys.stderr)
    print(time.time())
    return {'time': time.time()}

# test
@app.route('/raw')
def get_raw():
    
    # SOLUTION 1:
    # with open("C:\\Users\\edrin\\Documents\\#COMPUTER SCIENCE\\CS3072 & CS3605 - FYP\\Resources & Links\\State Of JavaScript [DATASET]\\state_of_js_2016_test.ndjson") as f:
    #     for line in f:
    #         j_content = json.loads(line)

    # SOLUTION 2:
    # data = []
    # with open('file') as f:
    #     for line in f:
    #         data.append(json.loads(line))

    # SOLUTION 3:
    # contents = open("C:\\Users\\edrin\\Documents\\#COMPUTER SCIENCE\\CS3072 & CS3605 - FYP\\Resources & Links\\State Of JavaScript [DATASET]\\state_of_js_2016_test.ndjson", "r").read() 
    # data = [json.loads(str(item)) for item in contents.strip().split('\n')]

    # print(len(data))
    # print(type(data))

    #SOLUTION 4:
    data_frame = pd.read_json('C:\\Users\\edrin\\Documents\\#COMPUTER SCIENCE\\CS3072 & CS3605 - FYP\\Resources & Links\\State Of JavaScript [DATASET]\\state_of_js_2016_test.ndjson', lines=True)
    # 'chuncks' param to read large file needed(?) 


    print(type(data_frame))
    print(data_frame.head())
    print(data_frame['tools'])
    print(data_frame.columns)

    return {'raw': 'foo'}

# config
if __name__ == '__main__':
    app.run(debug=True)