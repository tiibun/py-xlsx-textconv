import warnings
import openpyxl
from openpyxl import Workbook
from openpyxl.cell.cell import Cell

from py_xlsx_textconv.output import output
from .parse_macro import parse_macro


def convert(filename: str, data_only: bool = True):
    warnings.simplefilter('ignore')
    workbook: Workbook = openpyxl.open(filename, read_only=True, data_only=data_only)
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
    parse_macro(filename)


def rstrip_empty(list: list):
    i = len(list)
    while i > 0 and list[i - 1] == '':
        i -= 1
    return list[:i]
