import yaml


def open_ymlf(path) -> dict:
    with open(path) as file:
        return yaml.load(file, yaml.Loader)

print(open_ymlf('/home/ttehasi/python-project-50/tests/test_data/file2.yml'))