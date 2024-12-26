import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(sample_transactions):
    # Получаем транзакции с валютой "USD"
    usd_transactions = filter_by_currency(sample_transactions, "USD")

    # Проверяем, что первые две транзакции имеют валюту USD
    transaction = next(usd_transactions)
    assert transaction['operationAmount']['currency']['code'] == 'USD'
    transaction = next(usd_transactions)
    assert transaction['operationAmount']['currency']['code'] == 'USD'

    # Пытаемся получить еще одну транзакцию с валютой USD
    with pytest.raises(StopIteration):
        next(usd_transactions)

    # Получаем транзакции с валютой EUR
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    transaction = next(eur_transactions)
    assert transaction['operationAmount']['currency']['code'] == 'EUR'
    with pytest.raises(StopIteration):
        next(eur_transactions)



def test_transaction_descriptions(sample_transactions):
    # Создаем генератор транзакций возвращающий описание
    descriptions = transaction_descriptions(sample_transactions)

    # Получаем первые 4 описания и проверяем их
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
#     assert next(descriptions) == "Перевод с карты на карту"
#
    # Проверка на то, что генератор завершился после всех транзакций
    with pytest.raises(StopIteration):
        next(descriptions)


# Тест для проверки генератора номеров банковских карт
def test_card_number_generator():
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    # Собираем результаты генератора в список
    result = list(card_number_generator(1, 5))

    # Проверяем, что результат совпадает с ожидаемым
    assert result == expected


# Тест для проверки генератора с большими диапазонами
def test_large_range():
    # Ожидаемый список номеров карт для диапазона от 9990 до 9995
    expected = [
        "0000 0000 0000 9990",
        "0000 0000 0000 9991",
        "0000 0000 0000 9992",
        "0000 0000 0000 9993",
        "0000 0000 0000 9994",
        "0000 0000 0000 9995"
    ]

    # Собираем результаты генератора в список для диапазона от 9990 до 9995
    result = list(card_number_generator(9990, 9995))

    # Проверяем, что результат совпадает с ожидаемым
    assert result == expected