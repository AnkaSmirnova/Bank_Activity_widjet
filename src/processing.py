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
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Union[str, int]]], reverse: bool = True) -> List[Dict[str, Union[str, int]]]:
    """
    Функция сортирует список словарей по дате (ключ 'date').

    :data: список словарей, где ключи и значения представлены строками.
    :reverse: если True — сортировка по убыванию, если False — по возрастанию (по умолчанию True)
    :return: новый отсортированный список словарей
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
