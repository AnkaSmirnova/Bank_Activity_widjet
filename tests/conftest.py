import pytest


# Фикстура для корректного номера карты
@pytest.fixture
def valid_card_number() -> str:
    return "1234567812345678"


# Фикстура для некорректного номера карты (слишком короткий)
@pytest.fixture
def invalid_card_number_short() -> str:
    return "12345"


# Фикстура для некорректного номера карты (с нецифровыми символами)
@pytest.fixture
def invalid_card_number_non_digits() -> str:
    return "12345678ABCD5678"


# Фикстура для корректных дат
@pytest.fixture
def valid_dates() -> list:
    return [
        ("2024-12-20T14:30:45.123456", "20.12.2024"),
        ("2022-03-15T08:00:00.000000", "15.03.2022"),
    ]


# Фикстура для некорректных дат
@pytest.fixture
def invalid_dates() -> list:
    return [
        ("2024-12-20 14:30:45", "Некорректный формат даты."),
        ("2024-12-20T14:30", "Некорректный формат даты."),
        ("2024-12-32T14:30:45", "Некорректный формат даты."),
        ("20th December 2024", "Некорректный формат даты."),
        ("", "Некорректный формат даты."),
    ]


# Фикстура с тестовыми данными
@pytest.fixture
def transactions() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
