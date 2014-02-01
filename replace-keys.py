from os import listdir
from os.path import join, isfile, isdir
from json import loads
import string
import sys


def find(path, fileOp, arg):
    for item in listdir(path):
        f = join(path, item)
        if isfile(f):
            fileOp(f, arg)
        elif isdir(f):
            find(f, fileOp, arg)


def instData(filename, data):
    try:
        with open(filename, 'r') as f:
            fileStr = f.read()
    except UnicodeDecodeError:
        print('Ignoring {}. (UnicodeDecodeError)'.format(filename))
        return

    for key, value in data.items():
        fileStr = fileStr.replace('{' + key + '}', value)

    with open(filename, 'w') as f:
        f.write(fileStr)


def main():
    try:
        files = sys.argv[1]
        dataFileName = sys.argv[2]
    except IndexError:
        sys.exit('Usage: python3 replace-keys.py [directory] [data.json]')

    try:
        with open(dataFileName, 'r') as dataFile:
            dataStr = dataFile.read()
        data = loads(dataStr)

    except:
        print("Error in processing JSON file: ", sys.exc_info()[0])
        raise

    find(files, instData, data)

    print('All keys in {} replaced.'.format(files))


if __name__ == '__main__':
    main()
