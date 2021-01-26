import pytest


def test_foo():
    assert 1 + 1 == 2


def test_fail():
    print("HELLO")
    assert 1 == 0


@pytest.mark.skip
def test_skip():
    pass
