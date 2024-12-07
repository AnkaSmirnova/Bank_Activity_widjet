from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

"""Программа запрашивает у пользователя ввод номера карты и
номера счета, затем выводит маскированные значения."""


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))