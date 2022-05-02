from oletools.olevba import VBA_Parser
from py_xlsx_textconv.output import output


def parse_macro(filename: str):
    with open(filename) as f:
        content = f.read()
        vbaparser = VBA_Parser(filename, data=content)
        if not vbaparser.detect_vba_macros():
            return

        for filename, stream_path, vba_filename, vba_code in vbaparser.extract_macros(
        ):
            output('OLE stream  :', stream_path)
            output('VBA filename:', vba_filename)
            output(vba_code)
