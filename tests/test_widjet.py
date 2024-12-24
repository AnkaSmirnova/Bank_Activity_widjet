import pytest

from src.widget import get_date, mask_account_card


# Тестирование корректной маскировки номеров карт
@pytest.mark.parametrize(
    "info_cards, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_valid(info_cards: str, expected: str) -> None:
    result = mask_account_card(info_cards)
    assert result == expected


# Тестирование некорректных входных данных для маскировки карт
@pytest.mark.parametrize(
    "info_cards, expected_error",
    [
        ("Visa", "Некорректный ввод.."),
        ("7158300734726758", "Некорректный ввод.."),
        ("Visa Classic", "Некорректный ввод.."),
    ],
)
def test_mask_account_card_invalid(info_cards: str, expected_error: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(info_cards)


# Тестирование номеров карт с пробелами
@pytest.mark.parametrize("info_cards, expected", [("Visa 1234 5678 9012 3456", "Visa 1234 56** **** 3456")])
def test_mask_account_card_with_spaces_and_dashes(info_cards: str, expected: str) -> None:
    assert mask_account_card(info_cards)


# Тестирование нераспознанных типов карт
@pytest.mark.parametrize("type_card", ["Visa", "карта", "master card"])
def test_mask_account_type_card_invalid(type_card: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(type_card)


# Тестирование корректных дат с использованием фикстуры
def test_valid_date(valid_dates: list) -> None:
    for date, expected in valid_dates:
        assert get_date(date) == expected


# Тестирование некорректных дат с использованием фикстуры
def test_invalid_date_format(invalid_dates: list) -> None:
    for date, expected in invalid_dates:
        with pytest.raises(ValueError):
            assert get_date(date)
