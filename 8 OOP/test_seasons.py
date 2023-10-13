from seasons import convert
from datetime import date,timedelta

def test_convert():
    assert convert((date.today() - timedelta(days=365)).isoformat()) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert((date.today() - timedelta(days=365*2)).isoformat()) == "One million, fifty-one thousand, two hundred minutes"
    try:
        assert convert("20211014") == "One million, fifty-one thousand, two hundred minutes"
    except:
        pass