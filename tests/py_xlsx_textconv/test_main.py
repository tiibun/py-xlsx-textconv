from os.path import dirname, join
from unittest.mock import Mock, patch
from py_xlsx_textconv.__main__ import main


def test_main():
    filename = join(dirname(__file__), '..', 'test.xlsx')
    with patch('sys.argv', ['', filename]):
        with patch('py_xlsx_textconv.__main__.convert', Mock()) as mock:
            main()
        mock.assert_called_once_with(filename)


def test_main_no_exists():
    with patch('sys.argv', ['', "not_exists.xlsx"]):
        with patch('py_xlsx_textconv.__main__.convert', Mock()) as mock:
            main()
        mock.assert_not_called()
