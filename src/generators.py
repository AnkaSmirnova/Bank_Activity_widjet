def filter_by_currency(transactions, currency_code):
    """Возвращает итератор, который поочередно выдает транзакции с заданной валютой"""
    for transaction in transactions:
        # Проверяем, что валюта в операции соответствует заданному коду
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


# transactions_lst = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     },
#     {
#         "id": 123456789,
#         "state": "EXECUTED",
#         "date": "2021-06-01T12:00:00",
#         "operationAmount": {
#             "amount": "200.00",
#             "currency": {
#                 "name": "EUR",
#                 "code": "EUR"
#             }
#         },
#         "description": "Оплата за услугу",
#         "from": "Счет 12345678901234567890",
#         "to": "Счет 98765432109876543210"
#     }
# ]
#
# usd_transactions = filter_by_currency(transactions_lst, "USD")
# # Получаем первые две транзакции с валютой USD
# for _ in range(2):
#     print(next(usd_transactions))
