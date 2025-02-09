import json

import yaml


def parse(data, tip):
    match tip:
        case 'json':
            with open(data) as file:
                return json.load(file)
        case '.yml':
            with open(data) as file:
                return yaml.load(file, yaml.Loader)
        case 'yaml':
            with open(data) as file:
                return yaml.load(file, yaml.Loader)
