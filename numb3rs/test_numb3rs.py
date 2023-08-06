from numb3rs import validate

def test_true():
    assert '1.0.56.54' == 'True'
    assert '255.0.255.0' == 'True'
    assert '1.1.1.1' == 'True'
    assert '99.97.156.254' == 'True'