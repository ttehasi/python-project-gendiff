from pathlib import Path

import pytest

from gendiff.gen_diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


actual_json_recurs = generate_diff(str(get_test_data_path('file11.json')),
                                   str(get_test_data_path('file22.json')))
actual_yml_recurs = generate_diff(str(get_test_data_path('file11.yml')),
                                  str(get_test_data_path('file22.yml')))
actual_json_plain = generate_diff(str(get_test_data_path('file11.json')),
                                   str(get_test_data_path('file22.json')),
                                  'plain')
actual_yml_plain = generate_diff(str(get_test_data_path('file11.yml')),
                                  str(get_test_data_path('file22.yml')),
                                 'plain')
actual_json_json = generate_diff(str(get_test_data_path('file11.json')),
                                   str(get_test_data_path('file22.json')),
                                 'json')
actual_yml_json = generate_diff(str(get_test_data_path('file11.yml')),
                                  str(get_test_data_path('file22.yml')),
                                'json')
actual_json = generate_diff(str(get_test_data_path('file1.json')),
                            str(get_test_data_path('file2.json')))
actual_yml = generate_diff(str(get_test_data_path('file1.yml')),
                           str(get_test_data_path('file2.yml')))


@pytest.mark.parametrize("result,actual,yam_act",
                         [(read_file('result_file1_file2.txt'),
                           actual_json, actual_yml)])
def test_generate_diff(result, actual, yam_act):
    assert actual == result
    assert yam_act == result


@pytest.mark.parametrize("result,actual,yam_act",
                         [(read_file('result_file11_file22.cpp'),
                           actual_json_recurs, actual_yml_recurs)])
def test_generate_diff_recurs(result, actual, yam_act):
    assert actual == result
    assert yam_act == result


@pytest.mark.parametrize("result,actual,yam_act",
                         [(read_file('result_plain.txt'),
                           actual_json_plain, actual_yml_plain)])
def test_generate_diff_plain(result, actual, yam_act):
    assert actual == result
    assert yam_act == result


@pytest.mark.parametrize("result,actual,yam_act",
                         [(read_file('result_json.json'),
                           actual_json_json, actual_yml_json)])
def test_generate_diff_json(result, actual, yam_act):
    assert actual == result
    assert yam_act == result
