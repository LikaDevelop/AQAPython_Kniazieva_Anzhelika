import pytest

x = 4
@pytest.mark.skip
def test_equals():
    assert x == 4

@pytest.mark.skipif(x > 5, reason='x should be less than 5 to run test')
def test_x():
    pass

def test_1():
    pass

def test_2():
    pass

@pytest.mark.smoke
def test_3():
    print('smoke test 1 (3)')
@pytest.mark.smoke
def test_4():
    print('smoke test 2 (4)')

@pytest.mark.regression
@pytest.mark.smoke
def test_5():
    pass