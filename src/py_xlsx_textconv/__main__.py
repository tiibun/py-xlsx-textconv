import argparse
from py_xlsx_textconv.run import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    filename = args.filename
    run(filename)

if __name__ == '__main__':
    main()
