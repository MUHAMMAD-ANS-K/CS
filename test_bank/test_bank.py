from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('Hello') == 0
def test_h():
    assert value('How are you?') == 20
    assert value('hi') == 20
def test_wouth():
    assert value('Greetings') == 100
    assert value('brosky') == 100
