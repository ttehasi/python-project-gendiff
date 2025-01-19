import yaml


def open_ymlf(path) -> dict:
    with open(path) as file:
        return yaml.load(file, yaml.Loader)
