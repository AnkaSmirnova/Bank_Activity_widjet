from src.widget import get_date, mask_account_card

"""Программа запрашивает у пользователя ввод номера карты или
номера счета, затем выводит маскированные значения."""


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_date("2024-03-11T02:26:18.671407"))
