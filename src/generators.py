from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
    """Возвращает итератор, который поочередно выдает транзакции с заданной валютой"""
    for transaction in transactions:
        # Проверяем, что валюта в операции соответствует заданному коду
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[Dict, None, None]:
    """Генератор, который поочередно возвращает описание каждой транзакции"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Заданный диапазон от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, end + 1):
        # Форматируем номер карты с ведущими нулями и разделителями
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:16]
