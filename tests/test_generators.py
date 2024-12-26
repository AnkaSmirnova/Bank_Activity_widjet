import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(sample_transactions):
    # Получаем транзакции с валютой "USD"
    usd_transactions = filter_by_currency(sample_transactions, "USD")

    # Проверяем, что первые две транзакции имеют валюту USD
    assert next(usd_transactions)['operationAmount']['currency']['code'] == 'USD'
    assert next(usd_transactions)['operationAmount']['currency']['code'] == 'USD'

    # Пытаемся получить еще одну транзакцию с валютой USD
    with pytest.raises(StopIteration):
        next(usd_transactions)

    # Получаем транзакции с валютой EUR
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    assert next(eur_transactions)['operationAmount']['currency']['code'] == 'EUR'
    with pytest.raises(StopIteration):
        next(eur_transactions)
