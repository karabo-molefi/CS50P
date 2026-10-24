from bank import value

def main():
    test_hello()
    test_h()
    test_other()
    test_case()


def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20
    assert value("howdy") == 20

def test_other():
    assert value("greetings") == 100
    assert value("salut") == 100

def test_case():
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("Greetings") == 100

if __name__ == "__main__":
    main()