from numb3rs import validate
def main():
    test_1()
    test_2()

def test_1():
    assert validate(r'127.0.0.1') == 'True'
    assert validate(r'255.255.255.255') == 'True'
    assert validate(r'140.247.235.144') == 'True'
    assert validate(r'256.255.255.255') == 'False'

def test_2():
    assert validate(r'cat') == 'False'
    assert validate(r'8.8.8') == 'False'
    assert validate(r'10.10.10.10.10') == 'False'
    assert validate(r'64.128.256.512') == 'False'
    assert validate(r'dog') == 'False'

if __name__ == '__main__':
    main()

