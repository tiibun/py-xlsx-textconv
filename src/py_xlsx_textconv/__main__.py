import argparse
from . import __version__
from .convert import convert

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='excel filename')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    args = parser.parse_args()

    filename = args.filename
    convert(filename)

if __name__ == '__main__':
    main()
