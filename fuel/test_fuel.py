import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    #with pytest.raises(ValueError):
     #   convert('3')
    #with pytest.raises(ValueError):
     #   convert('cat')