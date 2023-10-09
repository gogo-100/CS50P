from bank import value

def test_value():
    assert value("hello") == 0
    assert value("he") == 20
    assert value("Hi") == 20
    assert value("starstar") == 100
    assert value("kdksjfxs..") == 100
    assert value("123") == 100