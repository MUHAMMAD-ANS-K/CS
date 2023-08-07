from working import convert

def test_1():
    assert convert('9 AM to 9 AM') == '09:00 to 09:00'
    assert convert('10 PM to 9 AM') == '22:00 to 09:00'
    assert convert('12:39 AM to 12:42 PM') == '00:39 to 12:42'
    with pytest.raises(ValueError)