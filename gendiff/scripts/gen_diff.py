import json


def generate_diff(path_to_file):
    with open(path_to_file) as file:
        return json.load(file)
