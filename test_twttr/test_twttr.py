from twttr import shorten

def test_cvowels():
    assert shorten('twitter') == 'twttr'
    assert shorten('aeiou') == ''

def test_wvowels():
    assert shorten('twttr') == 'twttr'
    assert shorten('#$@1') == '#$@1'
def test_uvowels():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('ANS') == 'NS'

def test_punct():
    assert shorten(h)