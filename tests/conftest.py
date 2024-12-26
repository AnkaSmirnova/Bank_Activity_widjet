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


# Фикстура, с тестовыми данными для генераторов
@pytest.fixture
def sample_transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2021-06-01T12:00:00",
            "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 12345678901234567890",
            "to": "Счет 98765432109876543210",
        },
    ]
