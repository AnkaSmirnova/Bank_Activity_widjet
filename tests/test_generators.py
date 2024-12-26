import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Параметризированный тест для проверки фильтрации по валюте
@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("USD", 2),  # Ожидаем, что 2 транзакции будут с валютой USD
        ("EUR", 1),  # Ожидаем, что 1 транзакция будет с валютой EUR
        ("GBP", 0),  # Ожидаем, что не будет транзакций с валютой GBP
    ],
)
def test_filter_by_currency(sample_transactions: list, currency_code: str, expected_count: str) -> None:
    # Получаем транзакции с указанной валютой
    filtered_transactions = filter_by_currency(sample_transactions, currency_code)

    # Проверяем, что количество транзакций с указанной валютой соответствует ожидаемому
    count = 0
    for transaction in filtered_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == currency_code
        count += 1

    # Проверяем, что количество транзакций совпадает с ожидаемым
    assert count == expected_count


@pytest.mark.parametrize(
    "expected_descriptions",
    [
        # Создаем генератор транзакций возвращающий описание
        (["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]),
    ],
)
def test_transaction_descriptions(sample_transactions: list, expected_descriptions: list) -> None:
    # Создаем генератор, который возвращает описания транзакций
    descriptions = transaction_descriptions(sample_transactions)

    # Проверяем, что каждое описание соответствует ожидаемому
    for expected_description in expected_descriptions:
        assert next(descriptions) == expected_description

    # Проверка на то, что генератор завершился после всех транзакций
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест для генератора номеров банковских карт
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9990,
            9995,
            [
                "0000 0000 0000 9990",
                "0000 0000 0000 9991",
                "0000 0000 0000 9992",
                "0000 0000 0000 9993",
                "0000 0000 0000 9994",
                "0000 0000 0000 9995",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list) -> None:
    # Собираем результаты генератора в список
    result = list(card_number_generator(start, end))

    # Проверяем, что результат совпадает с ожидаемым
    assert result == expected
