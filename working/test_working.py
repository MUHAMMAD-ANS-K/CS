from working import convert

def test_1():
    assert convert('9 AM to 9 AM') == '9:00 to 9:00'
    assert convert('10 PM to 9 AM') == '22:00 to 9:00'
