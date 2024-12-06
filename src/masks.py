def get_mask_card_number(number_card: str) -> str:
    """Функция принимает номер карты в виде строки и возвращает его маску.
    Формат маски "XXXX XX** **** XXXX" """
    if len(number_card) != 16 or not number_card.isdigit():
        return "Номер карты должен быть длиной 16 цифр."
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Формат маски "**XXXX", видны последние 4 цифры."""
    if len(number_account) != 20 or not number_account.isdigit():
        return "Номер счета состоит из 20 цифр."
    return f"**{number_account[-4:]}"
