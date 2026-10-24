from plates import is_valid

def main():
    test_length()
    test_beginning_alphabetical()
    test_zero_placement()
    test_number_placement()
    test_puncuation()
    
def test_length():
    assert is_valid("GOODBYE") == False
    assert is_valid("B") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True

def test_beginning_alphabetical():
    assert is_valid("NO") == True
    assert is_valid("CS50") == True
    assert is_valid("123456") == False
    assert is_valid("A123") == False

def test_zero_placement():
    assert is_valid("ABC07") == False
    assert is_valid("AC70") == True

def test_number_placement():
    assert is_valid("CS50P") == False
    assert is_valid("ABC7D") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False

if __name__ == "__main__":
    main()