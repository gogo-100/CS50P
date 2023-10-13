from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("275.3.6.28") == False
    assert validate("kdksjfxs..") == False
    assert validate("123") == False
    assert validate("10.1.2.3.14") == False
    assert validate("25.3.776.28") == False
    assert validate("25.333.76.28") == False
    assert validate("25.3.77.285") == False