from numb3rs import validate

def test_1():
    assert validate('127.0.0.1') == 'True'
    assert validate('255.255.255.255') == 'True'
    assert validate('140.247.235.144') == 'True'
    assert validate('256.255.255.255') == 'False'





