import warnings
import openpyxl
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


def convert(filename):
    warnings.simplefilter('ignore')
    workbook = openpyxl.open(filename, read_only=True, data_only=True)
    for ws in workbook:
        ws_name = f'[{ws.title}]'
        has_rows = False
        for row in ws.iter_rows():
            values = [ws_name]
            for cell in row:
                value = cell.value
                if value is None:
                    value = ''
                elif isinstance(value, str):
                    value = value.replace('\n', '\\n')
                else:
                    value = str(value)
                values.append(value)

            values = rstrip_empty(values)
            text = '\t'.join(values)
            output(text)
            has_rows = True
        if not has_rows:
            # print only sheet name
            output(ws_name)
    workbook.close()


def rstrip_empty(list: list):
    i = len(list)
    while i > 0 and list[i - 1] == '':
        i -= 1
    return list[:i]
