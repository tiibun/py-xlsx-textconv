from oletools.olevba import VBA_Parser
from py_xlsx_textconv.output import output

def parse_macro(filename: str):
    vbaparser = VBA_Parser(filename)
    if not vbaparser.detect_vba_macros():
        return

    for filename, _stream_path, vba_filename, vba_code in vbaparser.extract_macros(
    ):
        output(f'[VBA filename]\t{vba_filename}')
        output(vba_code)
