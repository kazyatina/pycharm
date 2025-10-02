import os
import re

from src.read_excel import read_excel_file

path_to_excel = os.path.join(os.path.dirname(__file__), "../data/transactions_excel.xlsx")

filepath_xlsx = read_excel_file(path_to_excel)


def process_bank_search(excel_file_path, search: str):
    """Возвращает список транзакций, описания которых содержат заданную строку"""
    try:
        if not excel_file_path:
            raise ValueError("Список словарей пуст")
        else:
            operation_list = []
            for string in excel_file_path:
                description = string.get("description")
                if description and isinstance(description, str):  # Проверяем, что description не None
                    match = re.search(search, description, flags=re.IGNORECASE)
                    if match:
                        operation_list.append(string)

        return operation_list

    except ValueError:
        return "Совпадений нет."


# result = process_bank_search(filepath_xlsx, "Открытие вклада")
# print(result)
