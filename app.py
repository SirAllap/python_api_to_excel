import json
from flask import Flask

app = Flask(__name__)

json_data_path = "./data.json"

def get_json_data():
    with open(json_data_path, 'r') as json_file:
        data = json.load(json_file)
    return data

@app.route('/', methods=['GET'])
def root():
    return "I'm the root of the API"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
