import json

json_data_path = "./data.json"

def get_json_data():
    with open(json_data_path, 'r') as json_file:
        data = json.load(json_file)
    return data

print(get_json_data())
