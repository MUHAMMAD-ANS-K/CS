import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('3')
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('')
    with pytest.raises(ValueError):
        convert('/')
def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'