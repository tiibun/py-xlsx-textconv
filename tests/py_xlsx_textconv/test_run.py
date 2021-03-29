from io import StringIO
from os.path import dirname, join
from unittest.mock import patch
from py_xlsx_textconv.run import run


def test_run():
    with patch('py_xlsx_textconv.run.stdout',
               new_callable=StringIO) as mock_stdout:
        run(join(dirname(__file__), '..', 'test.xlsx'))
        assert mock_stdout.getvalue() == '''[Sheet1]\tA1\tB1\t\t
[Sheet1]\tA2\t\tC2\t
[Sheet1]\tA2\t\t\tD3\\nLF
[Sheet2]
'''
