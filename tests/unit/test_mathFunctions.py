import pytest

from functions.mathFunctions import cube_method
from functions.mathFunctions import square_method
from functions.mathFunctions import sum_method

def test_square_method():
    assert square_method(2) == 4

#TODO: Disable pytest.mark.skip by commenting it
@pytest.mark.skip
def test_cube_method():
    assert cube_method(2) == 8

#TODO: Correct the Assertion Logic
def test_sum_method():
    assert sum_method(2,4) == 7
