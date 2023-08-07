from working import convert
import pytest
def test_1():
    assert convert('9 AM to 9 AM') == '09:00 to 09:00'
    assert convert('10 PM to 9 AM') == '22:00 to 09:00'
    assert convert('12:39 AM to 12:42 PM') == '00:39 to 12:42'

def test_2():
    with pytest.raises(ValueError):
        convert('9AM to 10PM')
    with pytest.raises(ValueError):
        convert('10 AM to 12:60 AM')
    with pytest.raises(ValueError):
        convert('9:30 am 10:40 pm')
