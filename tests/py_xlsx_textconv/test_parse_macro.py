from io import StringIO
from os.path import dirname, join
from unittest.mock import patch

from py_xlsx_textconv.parse_macro import parse_macro


def test_parse_macro():
    with patch('py_xlsx_textconv.output.stdout',
               new_callable=StringIO) as mock_stdout:
        parse_macro(join(dirname(__file__), '..', 'test.xlsm'))
        assert mock_stdout.getvalue() == '''[VBA filename]\tModule1
Attribute VB_Name = "Module1"\r
Option Explicit\r
\r
Sub Macro1()\r
Attribute Macro1.VB_ProcData.VB_Invoke_Func = " \\n14"\r
    Range("A1").Select\r
End Sub\r


[VBA filename]	ThisWorkbook\r
Attribute VB_Name = "ThisWorkbook"\r
Attribute VB_Base = "0{00020819-0000-0000-C000-000000000046}"\r
'''
