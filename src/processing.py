from typing import Dict, List, Union


def filter_by_state(
    data: List[Dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """
    Функция фильтрует список словарей, возвращая только те словари,
    у которых ключ 'state' соответствует заданному значению.

    :data: список словарей, где ключи и значения представлены строками.
    :state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: новый список словарей, которые соответствуют заданному состоянию
    """

    if state == "":
        state = "EXECUTED"

    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Union[str, int]]], reverse: bool = True) -> List[Dict[str, Union[str, int]]]:
    """
    Функция сортирует список словарей по дате (ключ 'date').

    :data: список словарей, где ключи и значения представлены строками.
    :reverse: если True — сортировка по убыванию, если False — по возрастанию (по умолчанию True)
    :return: новый отсортированный список словарей
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
