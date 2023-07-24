import pytest

@pytest.fixture(scope='function')
def my_first_fixture_placed_in_package():
    print('Setup before each test')
    yield
    print('TearDown after each test')


@pytest.fixture(scope='class')
def fixture_for_class():
    print('\nSetup before class')
    yield ['my', 'class', 'fixture', 'text']
    print('\nTear down after class')