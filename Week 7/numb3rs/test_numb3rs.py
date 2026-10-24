from numb3rs import validate

def main():
    test_length()
    test_period()
    test_range()

def test_length():
    assert validate("1.2.3.4") == True
    assert validate("0.1.2.3") == True
    assert validate("1.2.3.4.5") == False

def test_period():
    assert validate("1.2.3.4.") == False
    assert validate(".1.2.3.4.") == False
    assert validate(".1.2.3.4") == False

def test_range():
    assert validate("256.257.258.259") == False
    assert validate("250.257.258.259") == False
    assert validate("-256.257.258.259") == False
    assert validate("-1.-2.-3.-4") == False
    assert validate("255.200.100.0") == True

