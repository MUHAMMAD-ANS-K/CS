from numb3rs import validate

def test_true():
    assert validate('1.0.56.54') == 'True'
    assert validate('255.0.255.0') == 'True'
    assert validate('1.1.1.1') == 'True'
    assert validate('99.97.156.254') == 'True'


def test_false():
    assert validate('cat') == 'False'
    assert validate('256.45.23.0') == 'False'
    assert validate('222.3.2.cat') == 'False'
    assert validate('#.99.8.44') == 'False'
    assert validate('233.32.2322') == 'False

