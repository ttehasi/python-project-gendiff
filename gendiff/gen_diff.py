import json
import pathlib


def open_f(path_to_file) -> dict:
    with open(path_to_file) as file:
        return json.load(file)


def generate_diff(file1, file2):
    file1 = open_f(file1)
    file2 = open_f(file2)
    sorted_keys_f1 = sorted(list(file1))
    sorted_keys_f2 = sorted(list(file2))
    res = '''{
'''
    for i in sorted_keys_f1:
        if i in sorted_keys_f2:
            if file1[i] == file2[i]:
                res += f'    {i}: {file1[i]}\n'
            else:
                res +=f'''  - {i}: {file1[i]}
  + {i}: {file2[i]}\n'''
        else:
            res += f'  - {i}: {file1[i]}\n'
    for i in sorted_keys_f2:
        if i not in sorted_keys_f1:
            res += f'  + {i}: {file2[i]}\n'
    res += '}'
    return res
