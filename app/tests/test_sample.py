import pytest

def func(x):
    return x + 5

def test_method():
    assert func(5) == 10