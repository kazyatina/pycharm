from typing import Iterator, Any

transactions_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list, currency_list: str) -> Iterator[Any] | str | list[Any]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""

    transaction = [trans for trans in transactions if trans["operationAmount"]["currency"]["code"] == "USD"]
    if not transactions or not transaction:
        return 'Транзакций нет.'
    return transaction


usd_transactions = filter_by_currency(transactions_list, "USD")
iterator_1 = iter(usd_transactions)  # Преобразуем список в итератор
for _ in range(2):  # Как узнать какой диапозон ставить, если спискок огромный?
    if _ != "USD":
        print("Операций нет.")
    print(next(iterator_1))


# for x in iterator_1: - Почему выводит только 1 транзакцию, а не 2?
#     print(next(iterator_1))


def transaction_descriptions(transactions: list) -> list[Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции
    по очереди."""
    descriptions = [transactions["description"] for transactions in transactions]
    return descriptions


descriptions_list = transaction_descriptions(transactions_list)
iterator_2 = iter(descriptions_list)
for _ in range(4):
    print(next(iterator_2))


# for x in iterator_2: - Почему выводит только 2 описания, а не 4?
#     print(next(iterator_2))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров карт в диапазоне [start, end]."""
    for number in range(start, end + 1):
        # Форматируем число в 16-значное с ведущими нулями
        max_width = 16
        card_num = f"{number:0{max_width}}"
        # Разбиваем на группы по 4 цифры
        formatted = " ".join([card_num[i: i + 4] for i in range(0, 16, 4)])
        yield formatted


print(list(card_number_generator(0, 5)))
