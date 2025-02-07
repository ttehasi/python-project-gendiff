import json

import yaml

from gendiff.formatters.json import gen_diff_json
from gendiff.formatters.plain import gen_diff_plain
from gendiff.formatters.stylish import gen_diff_stylish
from gendiff.pars_data import parse


def difference(file1, file2):
    result = {}
    if isinstance(file1, dict) and isinstance(file2, dict):
        keys1 = sorted(list(file1.keys()))
        keys2 = sorted(list(file2.keys()))
        keys12 = sorted(set(keys1 + keys2))
        for i in keys12:
            if i in keys1 and i in keys2:
                if isinstance(file1[i], dict) and isinstance(file2[i], dict):
                    result[i] = ('nested', difference(file1[i], file2[i]))
                else:
                    if file1[i] == file2[i]:
                        result[i] = ('unchanged', file1[i])
                    else:
                        result[i] = ('changed', file1[i], file2[i])
            if (i in keys1) and (i not in keys2):
                result[i] = ('removed', file1[i])
            if (i not in keys1) and (i in keys2):
                result[i] = ('added', file2[i])
    return result


def generate_diff(file1, file2, format_name='stylish'):
    if str(file1)[-5:] == '.json' and str(file2)[-5:] == '.json':
        file1 = json.load(parse(file1))
        file2 = json.load(parse(file2))
    else:
        file1 = yaml.load(parse(file1), yaml.Loader)
        file2 = yaml.load(parse(file2), yaml.Loader)
    diff = difference(file1, file2)
    match format_name:
        case None:
            return gen_diff_stylish(diff)
        case 'stylish':
            return gen_diff_stylish(diff)
        case 'plain':
            return gen_diff_plain(diff)
        case 'json':
            return gen_diff_json(diff)
