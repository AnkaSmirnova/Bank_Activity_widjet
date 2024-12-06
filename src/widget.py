from masks import get_mask_card_number, get_mask_account

def mask_account_card(info_cards: str) -> str:
    """Функция принимает строку, содержащую тип и номер (карты или счета).
    В зависимости от типа данных, возвращает замаскированный номер."""
    info_card = info_cards.split()

    if len(info_card) != 2:
        return "Неверный формат. Ожидается тип и номер"

    type_card, number_cards = info_card

    if type_card.lower() in ['visa', 'maestro', 'mastercard']:
        return get_mask_card_number(number_cards)
    elif type_card.lower() == 'счет':
        return get_mask_account(number_cards)
    else:
        return "Неизвестный тип. Поддерживаемые типы: карта, счет."

from datetime import datetime

def get_date(date: str) -> str:
    """ Функция принимает строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    и возвращает строку с датой в формате "DD.MM.YYYY."""
    try:
        date_of_operation = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_of_operation.strftime("%d.%m.%Y")

    except ValueError:
        return "Некорректный формат даты."