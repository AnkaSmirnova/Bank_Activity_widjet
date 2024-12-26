import pytest

from src.generators import filter_by_currency, transaction_descriptions


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
