from plates import is_valid

def test_length():
    assert is_valid('H') == False
    assert is_valid('HI') == True
    assert is_valid('yourname') == False
def test_12alpha():
    assert is_valid('12hi') == False
    assert is_valid('HI0') == False
    assert is_valid('Ho2') == True
    assert is_valid('2HO') == False
    assert is_valid('02') == False

def test_numbers():
    assert is_valid('CS50') == True
    assert is_valid('NE8O') == False
    assert is_valid('PI ') == False
    assert is_valid('hi.,!') == False