from um import count

def test_1():
    assert count('um umu um') == 2
    assert count('um.?') == 1
    assert count('yummy') == 0
    assert count('0um3') == 0
    assert count('UM, I am sorry,um') == 2