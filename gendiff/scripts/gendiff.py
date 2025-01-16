import argparse

from gendiff.gen_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration files 
        and shows a difference.'''
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    diff = generate_diff(parser.parse_args().first_file,
                         parser.parse_args().second_file)
    return diff


if __name__ == "__main__":
    main()
