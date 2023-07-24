import pytest
import logging

x = 4
@pytest.mark.skip
def test_equals():
    assert x == 4

@pytest.mark.skipif(x > 5, reason='x should be less than 5 to run test')
def test_x():
    pass

def test_1():
    pass


class TestFixtures:
    # def test_in_class_1(self, my_first_fixture_placed_in_package):
    #     print('test_1 does something')
    #
    # def test_in_class_2(self, my_first_fixture_placed_in_package):
    #     print('test_2 does something')

    def test_in_class_1(self, fixture_for_class):
        assert 'my' in fixture_for_class

    def test_in_class_2(self, fixture_for_class):
        logging.error('test_2 does something')
        print('test_2 does something')