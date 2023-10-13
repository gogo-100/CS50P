from jar import Jar


def test_init():
    jar1 = Jar()
    jar2 = Jar(10)
    assert jar1.capacity == 12
    assert jar2.capacity == 10

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(5)
    assert jar.size == 9

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar.size == 8
    jar.withdraw(5)
    assert jar.size == 3