import pytest
from lib.parsers.api_parser import APIParser

from os import path


def test_parser():
    parser = APIParser(
        "https://jsonplaceholder.typicode.com/posts/1/comments", "structured")

    ret = parser.parse()

    assert ret.strip() != ""

    parser = APIParser(
        "https://jsonplaceholder.typicode.com/posts/1/comments", "flat")

    ret = parser.parse()

    assert ret.strip() != ""
