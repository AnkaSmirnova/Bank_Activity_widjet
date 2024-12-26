def filter_by_currency(transactions, currency_code):
    """Возвращает итератор, который поочередно выдает транзакции с заданной валютой"""
    for transaction in transactions:
        # Проверяем, что валюта в операции соответствует заданному коду
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который поочередно возвращает описание каждой транзакции"""
    for transaction in transactions:
        yield transaction.get("description")

