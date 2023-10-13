from um import count

def test_count():
    assert count("um") == 1
    assert count("yum") == 0
    assert count("um,world") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks for the um album.") == 2