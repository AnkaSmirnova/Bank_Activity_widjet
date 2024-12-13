from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_cards: str) -> str:
    """Функция принимает строку, содержащую тип и номер (карты или счета).
    В зависимости от типа данных, возвращает замаскированный номер."""
    info_card = info_cards.split()

    if len(info_card) > 2:
        type_card = info_card[0] + " " + info_card[1]
    else:
        type_card, number_cards = info_card

    number_cards = info_card[-1]

    if info_card[0].lower() in ["visa", "maestro", "mastercard"]:
        masked_number = get_mask_card_number(number_cards)
        return f"{type_card} {masked_number}"
    elif info_card[0].lower() == "счет":
        masked_number = get_mask_account(number_cards)
        return f"{type_card} {masked_number}"
    else:
        return "Неизвестный тип. Поддерживаемые типы: карта, счет."


def get_date(date: str) -> str:
    """Функция принимает строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    и возвращает строку с датой в формате "DD.MM.YYYY."""
    try:
        date_of_operation = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_of_operation.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректный формат даты."
