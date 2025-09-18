import json
import os


def fin_trans(link_to_j_file="../data/operations.json"):
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""
    if not os.path.exists(link_to_j_file):
        return []  # Файл не существует
    try:
        with open(link_to_j_file, "r", encoding="utf8") as file:
            try:
                fin_operation = json.load(file)
            except json.JSONDecodeError:
                return []  # Ошибка декодирования JSON, файл поврежден или пуст
            if isinstance(fin_operation, list):
                return fin_operation  # Возвращаем список словарей
            else:
                return []  # Файл содержит не список
    except Exception:
        return []  # Обработка любых других ошибок чтения файла
