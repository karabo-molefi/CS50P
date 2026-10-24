from twttr import shorten

def main():
    test_uppercase()
    test_lowercase()
    test_numeric()
    test_no_replacement()
    test_punctuation()
    test_printing_uppercase()


def test_uppercase():
    for v in ["A", "E", "I", "O", "U"]:
        assert shorten(v) == ""

def test_lowercase():
    for v in ["a", "e", "i", "o", "u"]:
        assert shorten(v) == ""

def test_numeric():
    assert shorten("50") == "50"

def test_no_replacement():
    for v in ["A", "E", "I", "O", "U"]:
        assert shorten(v) != v

def test_punctuation():
    for p in ["!", ".", "?", ","]:
        assert shorten(p) == p

def test_printing_uppercase():
    assert shorten("hi") == "h"

if __name__ == "__main__":
    main()