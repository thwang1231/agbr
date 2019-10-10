import json


def print_json(json_obj):
    print(json.dumps(json_obj, indent=4, sort_keys=True))


def load_json(json_path):
    with open(json_path) as json_file:
        return json.load(json_file)

def load_data(data_path):
    with open(data_path) as data_file:
        return [edge.split() for edge in data_file.readlines()]
