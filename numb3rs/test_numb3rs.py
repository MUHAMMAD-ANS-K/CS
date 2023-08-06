from numb3rs import validate



def test_2():
    assert validate('cat') == 'False'
    assert validate('8.8.8') == 'False'
    assert validate('10.10.10.10.10') == 'False'
    assert validate('64.128.256.512') == 'False'
    assert validate('dog') == 'False'



