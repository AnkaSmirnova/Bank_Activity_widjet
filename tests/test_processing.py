import pytest

from src.processing import filter_by_state, sort_by_date

# Тестирование фильтрацию по значению state
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]),
    # Тест для состояния "FAILED", когда таких записей нет
    ("FAILED", []),  # В случае отсутствия таких записей
                     # Пустая строка по умолчанию фильтруется по EXECUTED
    ("", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ])
])
def test_filter_by_state(transactions, state, expected):
    result = filter_by_state(transactions, state)
    assert result == expected


# Тестирование сортировки транзакций по дате
@pytest.mark.parametrize("reverse, expected", [
    (True, [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]),
    (False, [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ])
])
def test_sort_by_date(transactions, reverse, expected):
    result = sort_by_date(transactions, reverse)
    assert result == expected
