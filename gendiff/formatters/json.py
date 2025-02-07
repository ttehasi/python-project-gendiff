import json


def gen_diff_json(value):
    result = json.dumps(value, sort_keys=True, indent=2)
    return result