from numb3rs import validate

def test_true():
    assert validate('1.0.56.54') == 'True'
    assert validate('255.0.255.0') == 'True'
    assert validate('1.1.1.1') == 'True'
    assert validate('99.97.156.254') == 'True'