import pytest


from src.masks import get_mask_account, get_mask_card_number

# Фикстуры
@pytest.fixture
def valid_card_number():
    return "1234567812345678"

@pytest.fixture
def invalid_card_number_short():
    return "12345"

@pytest.fixture
def invalid_card_number_non_digits():
    return "12345678ABCD5678"

# Тесты
def test_valid_card_number(valid_card_number):
    assert get_mask_card_number(valid_card_number) == "1234 56** **** 5678"

def test_invalid_card_number_short(invalid_card_number_short):
    assert get_mask_card_number(invalid_card_number_short) == "Номер карты должен быть длиной 16 цифр."

def test_invalid_card_number_non_digits(invalid_card_number_non_digits):
    assert get_mask_card_number(invalid_card_number_non_digits) == "Номер карты должен быть длиной 16 цифр."

# Тест с параметризацией
@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("12345", "Номер счета состоит из 20 цифр."),
    ("12345ABCDE678901234567890", "Номер счета состоит из 20 цифр."),
    ("", "Номер счета состоит из 20 цифр."),
])
def test_account_number(account_number, expected):
    assert get_mask_account(account_number) == expected


