import sys

# force LF on Windows
stdout = open(sys.__stdout__.fileno(),
              mode=sys.__stdout__.mode,
              buffering=1,
              encoding=sys.__stdout__.encoding,
              errors=sys.__stdout__.errors,
              newline='\n',
              closefd=False)


def output(values: any):
    print(values, file=stdout)
