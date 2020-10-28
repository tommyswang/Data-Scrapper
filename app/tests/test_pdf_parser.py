import pytest
from lib.parsers.pdf_parser import PdfParser

from os import path


def test_parser():
    pdfPath = path.join(path.dirname(__file__), "form.pdf")
    parser = PdfParser(pdfPath)

    dfs = parser.parse()
    assert len(dfs) == 5

    pdfPath = path.join(path.dirname(__file__), "table.pdf")
    parser = PdfParser(pdfPath)

    dfs = parser.parse()
    assert len(dfs) == 4
