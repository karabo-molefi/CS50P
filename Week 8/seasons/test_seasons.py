import pytest
from datetime import date
from seasons import get_bday

def main():
    test_get()

def test_get():
    assert get_bday("2001-01-01") == date(2001, 1, 1)
    assert get_bday("2001-09-30") == date(2001, 9, 30)



if __name__ == "__main__":
    main()