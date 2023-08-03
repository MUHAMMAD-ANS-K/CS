import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ZeroDivisionError):
        1/0
    with pytest.raises(ValueError):
        3
    with pytest.raises(ValueError):
        cat