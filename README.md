# Виджет для отображения успешных банковских операций в личном кабинете клиента.

## Описание проекта

Этот проект разработан для использования в личном кабинете клиента крупного банка. Он предоставляет функциональность для подготовки данных о банковских операциях, таких как фильтрация, сортировка и маскирование номеров карт и счетов.
Эти данные будут использоваться для отображения информации о последних успешных операциях пользователя в виджет.

Проект включает несколько функций для обработки данных, работы с масками и преобразования дат, что помогает предоставить клиенту только необходимую информацию в удобном виде.

### Цель проекта

Основная цель проекта - создание функционала для фильтрации, сортировки и маскировки данных для отображения в виджет. Он включает следующие ключевые функции:
- Маскирование номеров карт и счетов для защиты конфиденциальной информации.
- Сортировка операций по дате.
- Фильтрация операций по состоянию (например, "EXECUTED").

## Структура проекта

- **src/processing.py** - содержит функции для фильтрации и сортировки данных о банковских операциях.
- **src/widget.py** - содержит функции для обработки данных в виджет, включая преобразование дат и маскирование данных.
- **src/masks.py** - содержит функции для маскировки номеров карт и счетов.
- **main.py** - основной файл для запуска программы.

## Установка

Для установки и управления зависимостями проекта используйте **Poetry**. Выполните следующие шаги:

1. Клонируйте репозиторий с проектом:
    ```
    git clone <https://github.com/AnkaSmirnova/Bank_Activity_widjet.git>
    ```

2. Перейдите в папку проекта:
    ```
    cd <Bank_Activity_Widget>
    ```

3. Установите зависимости с помощью Poetry:
    ```
    poetry install
    ```

4. Запустите проект:
    ```
    poetry run python src/main.py
    ```

## Использование

### Функции

1. **`get_mask_card_number(number_card: str) -> str`**
   Маскирует номер карты в формате "XXXX XX** **** XXXX".
   **Пример:**
      ```
      print(get_mask_card_number("5999414228426353"))  # "5999 41** **** 6353"
      ```

2. **`get_mask_account(number_account: str) -> str`**
   Маскирует номер счета в формате "**XXXX", показывая только последние 4 цифры.
   **Пример:**
      ```
      print(get_mask_account("1234567890123456"))  # "**3456"
      ```

3. **`mask_account_card(info_cards: str) -> str`**
   Возвращает замаскированный номер карты или счета из строки с типом и номером.
   **Пример:**
      ```
      print(mask_account_card("Visa Gold 5999414228426353"))  # "Visa Gold 5999 41** **** 6353"
      ```

4. **`get_date(date: str) -> str`**
   Преобразует дату из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в "DD.MM.YYYY".
   **Пример:**
      ```
      print(get_date("2024-03-11T02:26:18.671407"))  # "11.03.2024"
      ```

5. **`filter_by_state(data: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]`**
   Фильтрует список операций по состоянию.
   **Пример:**
      ```
      data = [{'state': 'EXECUTED', 'date': '2024-12-12'}, {'state': 'CANCELED', 'date': '2024-12-13'}]
      print(filter_by_state(data))  # [{'state': 'EXECUTED', 'date': '2024-12-12'}]
      ```

6. **`sort_by_date(data: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]`**
   Сортирует список операций по дате.
   **Пример:**
      ```
      data = [{'date': '2024-12-13'}, {'date': '2024-12-12'}]
      print(sort_by_date(data))  # [{'date': '2024-12-13'}, {'date': '2024-12-12'}]
      ```

---

## Запуск программы

Программа запрашивает у пользователя ввод номера карты или счета и выводит маскированные значения.

**Пример:**
```
python src/main.py