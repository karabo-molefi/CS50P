from um import count

def main():
    test_count()
    test_word_bound()
    test_case()


def test_count():
    assert count("um") == 1

def test_word_bound():
    assert count("yummy") == 0
    assert count("umm mum") == 0
    assert count("um mummy") == 1

def test_case():
    assert count("UM") == 1
    assert count("Um") == 1
    




if __name__ == "__main__":
    main()