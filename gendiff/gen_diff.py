import json

from gendiff.pars_yaml import open_ymlf


def open_f(path_to_file) -> dict:
    with open(path_to_file) as file:
        return json.load(file)


def stringify(value, lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{'    ' * lvl}{el}: '
            result += stringify(val, lvl + 1) + '\n'
        result += '    ' * (lvl - 1) + '}'
    else:
        if value is True:
            result = 'true'
        elif value is None:
            result = 'null'
        elif value is False:
            result = 'false'
        else:
            result = str(value)
    return result


def generate_diff(file1, file2, lvl=1):
    if isinstance(file1, str) and isinstance(file2, str):
        if str(file1)[-5:] == '.json' and str(file2)[-5:] == '.json':
            file1 = open_f(file1)
            file2 = open_f(file2)
        else:
            file1 = open_ymlf(file1)
            file2 = open_ymlf(file2)
    result = '{\n'
    if isinstance(file1, dict) and isinstance(file2, dict):
        keys1 = sorted(list(file1.keys()))
        keys2 = sorted(list(file2.keys()))
        keys12 = sorted(set(keys1 + keys2))
        for i in keys12:
            if i in keys1 and i in keys2:
                if isinstance(file1[i], dict) and isinstance(file2[i], dict):
                    result += f'{'    ' * lvl}{i}: '
                    result += generate_diff(file1[i], file2[i], lvl + 1) + '\n'
                else:
                    if file1[i] == file2[i]:
                        result += f'{'    ' * lvl}{i}: {file1[i]}' + '\n'
                    else:
                        result += (f'{'    ' * (lvl - 1) + '  - '}{i}: '
                                   f'{stringify(file1[i], lvl=lvl + 1)}') + '\n'
                        result += (f'{'    ' * (lvl - 1) + '  + '}{i}: '
                                   f'{stringify(file2[i], lvl=lvl + 1)}') + '\n'
            if (i in keys1) and (i not in keys2):
                result += (f'{'    ' * (lvl - 1) + '  - '}{i}: '
                           f'{stringify(file1[i], lvl=lvl + 1)}') + '\n'
            if (i not in keys1) and (i in keys2):
                result += (f'{'    ' * (lvl - 1) + '  + '}{i}: '
                           f'{stringify(file2[i], lvl=lvl + 1)}') + '\n'
        result += '    ' * (lvl - 1) + '}'
    return result
