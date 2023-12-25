import pytest

@pytest.fixture
def bad_word():
    return 'Масква'

@pytest.fixture
def good_word():
    return 'Москва'