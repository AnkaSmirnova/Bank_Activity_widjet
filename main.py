from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

"""Программа запрашивает у пользователя ввод номера карты и
номера счета, затем выводит маскированные значения."""

user_card_number = input("Введите номер карты (16 цифр): ")

user_account_number = input("Введите номер счета (20 цифр): ")

if __name__ == "__main__":
    print(get_mask_card_number(user_card_number))
    print(get_mask_account(user_account_number))



