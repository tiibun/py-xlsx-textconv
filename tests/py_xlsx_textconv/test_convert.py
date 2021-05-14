from io import StringIO
from os.path import dirname, join
from unittest.mock import patch
from py_xlsx_textconv.convert import convert


def test_convert():
    with patch('py_xlsx_textconv.convert.stdout',
               new_callable=StringIO) as mock_stdout:
        convert(join(dirname(__file__), '..', 'test.xlsx'))
        assert mock_stdout.getvalue() == '''[Sheet1]\tA1\tB1
[Sheet1]\tA2\t\tC2
[Sheet1]\tA2\t\t\tD3\\nLF
[Sheet2]
'''
