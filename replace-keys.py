from os import listdir
from os.path import join, isfile, isdir, expanduser
from json import loads
import string
import sys


def find(path, file_op, arg, ignore=[]):
    for item in listdir(path):
        f = join(path, item)
        if not item in ignore:
            if isfile(f):
                file_op(f, arg)
            elif isdir(f):
                find(f, file_op, arg)
        else:
            print('Ignoring {}'.format(f))

def insert_data(filename, data):
    try:
        with open(filename, 'r') as f:
            file_str = f.read()
    except UnicodeDecodeError:
        print('Ignoring {}. (UnicodeDecodeError)'.format(filename))
        return

    for key, value in data.items():
        file_str = file_str.replace('{'+key+'}', value)

    with open(filename, 'w') as f:
        f.write(file_str)

def extract_data(data_filename):
    try:
        with open(data_filename, 'r') as data_file:
            data_str = data_file.read()
        return loads(data_str)

    except:
       print('Error in processing JSON file: ', sys.exc_info()[0])
       raise

def replace(directory, filename, ignore=[]):
    data = extract_data(filename)
    find(directory, insert_data, data, ignore)
    print('All keys in {} replaced'.format(directory))


def main():
    try:
        directory = sys.argv[1]
        data_filename = sys.argv[2]
    except IndexError:
        sys.exit('Usage: python3 replace-keys.py [directory] [data.json]')

    replace(directory, data_filename)


if __name__ == '__main__':
    main()
