import os
from collections import Counter
from typing import List, Any

from src.read_excel import read_excel_file

path_to_excel = os.path.join(os.path.dirname(__file__), "../data/transactions_excel.xlsx")

filepath_xlsx = read_excel_file(path_to_excel)

description_list = []

def process_bank_operations(data:list[dict], categories:list)-> Counter[Any]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    if not data:
        raise ValueError("Список словарей пуст")
    else:
        for data_list in data:
            description = data_list.get("description", "")
            description_list.append(description)
        counted = Counter(description_list)
    return counted



result = process_bank_operations(filepath_xlsx, description_list)
print(result)