import pytest

import xlutility
from xlutility import function_operation


def multiply(x, y):
    return x * y


# @pytest.mark.parametrize('num1,num2,result', [(1, 2, 2), (2, 2, 4), (2, 3, 6)])
@pytest.mark.parametrize('num1,num2,result', function_operation())
def test_multiply(num1, num2, result):
    assert multiply(num1, num2) == result
