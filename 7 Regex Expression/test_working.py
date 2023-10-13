from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    try:
        assert convert("9:60 AM to 5:60 PM") == False
    except ValueError:
        pass
    try:
        assert convert("9:60 AM - 5:60 PM") == False
    except ValueError:
        pass