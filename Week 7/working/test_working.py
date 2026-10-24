import pytest
from working import convert

def main():
    test_convert()
    test_omission()
    test_range()

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_omission():
    try:
        convert("9 AM 5 PM")
    except ValueError:
        pass
    else:
        assert False

def test_range():
    try:
        convert("13 AM to 19 PM")
    except ValueError:
        pass
    else:
        assert False

if __name__ == "__main__":
    main()