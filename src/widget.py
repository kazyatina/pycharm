from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, и выводит маскировку.
    """
    if "счет" in info_card.lower():
        number_card = info_card[-10:]
        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"
    else:
        name_card = info_card[-16:]
        masked = get_mask_card_number(name_card)
        bank_name = info_card[:-16]
    return f"{bank_name} {masked}"


print(mask_account_card("Visa 7000792289606361"))


def get_date(date_str: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГ"""
    # Парсинг строки в объект даты
    parsed_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

    # Форматирование объекта даты в нужный формат
    formatted_date = parsed_date.strftime("%d.%m.%Y")

    return formatted_date  # Вывод: 11.03.2024


print(get_date("2024-03-11T02:26:18.671407"))
