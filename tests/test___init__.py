from bethesda_ini import foo


def test_foo():
    assert foo() == 0


def test_not_foo():
    assert not foo() == 1
