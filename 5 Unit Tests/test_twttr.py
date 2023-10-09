from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AIOUsEaue") == "s"
    assert shorten("e") == ""
    assert shorten("1111") == "1111"
    assert shorten("msr,go") == "msr,g"