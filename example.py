import pytest


def add(n1, n2):
    return n1 + n2


@pytest.mark.parametrize('num1,num2,result', [(1, 3, 4), ("Hello", " Pytest", "Hello Pytest")])
def test_func(num1, num2, result):
    assert add(num1, num2) == result
