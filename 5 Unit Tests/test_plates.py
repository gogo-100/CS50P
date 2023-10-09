from plates import is_valid

def test_is_valid():
    assert is_valid("CS50")
    assert not is_valid("CS05")
    assert not is_valid("CS50P")
    assert not is_valid("starstar")
    assert not is_valid("kdksjfxs..")
    assert not is_valid("123dd")
    assert not is_valid("023dd")
    assert not is_valid("H")
    assert  is_valid("JD")
    assert  is_valid("JD46")
    assert not is_valid("J46")
    assert not is_valid("JD.46")
    assert not is_valid("Jd4,6")
    assert not is_valid("JD 60")