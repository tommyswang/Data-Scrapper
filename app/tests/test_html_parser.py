import pytest
from lib.parsers.html_parser import HTMLParser

from os import path


def test_parser(mocker):

    # The sample table from the URL
    # ',Company,Contact,Country\n0,Alfreds Futterkiste,Maria Anders,Germany\n1,Centro comercial Moctezuma,Francisco Chang,Mexico\n2,Ernst Handel,Roland Mendel,Austria\n3,Island Trading,Helen Bennett,UK\n4,Laughing Bacchus Winecellars,Yoshi Tannamuri,Canada\n5,Magazzini Alimentari Riuniti,Giovanni Rovelli,Italy\n'
    parser = HTMLParser("https://www.w3schools.com/html/html_tables.asp")

    ret = parser.parse()

    assert len(ret) == 2

    lines = ret[0].splitlines()
    assert len(lines) == 5
