from plates import is_valid

def test_length():
    assert is_valid('H') == False
    assert is_valid('HI') == True
    assert is_valid('yourname') == False
def test_12alpha():
    assert is_valid('12h8i') == False
    assert is_valid('HI0') == False
    assert is_valid('Ho2') == True
    assert is_valid('2HO') == False
    assert is_valid('20') == False
    assert is_valid('HK') == True

def test_numbers():
    assert is_valid('CS50') == True
    assert is_valid('NE8O') == False
    assert is_valid('PI ') == False
    assert is_valid('hi.,!') == False