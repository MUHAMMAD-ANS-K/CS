from bank import value

def hello_test():
    assert value('hello') == '0'
    assert value('HELLO') == '0'
    assert value('Hello') == '0'