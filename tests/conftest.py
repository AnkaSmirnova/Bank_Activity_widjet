import pytest


@pytest.fixture
def valid_card_number():
    return "1234567812345678"

@pytest.fixture
def invalid_card_number_short():
    return "12345"

@pytest.fixture
def invalid_card_number_non_digits():
    return "12345678ABCD5678"