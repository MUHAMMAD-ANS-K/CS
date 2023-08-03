from bank import value

def test_hello():
    assert value('hello') == '0'
    assert value('HELLO') == '0'
    assert value('Hello') == '0'