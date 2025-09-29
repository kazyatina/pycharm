import json
import logging
import os

os.makedirs("logs", exist_ok=True)

# Настройка логирования
log_file_path = os.path.join("logs", "utils.log")
logging.basicConfig(
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="w", encoding="utf-8"),
        logging.StreamHandler(),  # Дополнительно выводим логи в консоль
    ],
)

logger = logging.getLogger("utils.log")


def fin_trans(link_to_j_file="../data/operations.json"):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""
    logger.info("Запуск работы функции")
    if not os.path.exists(link_to_j_file):
        logger.info("Файл не существует")
        return []  # Файл не существует
    try:
        with open(link_to_j_file, "r", encoding="utf8") as file:
            try:
                fin_operation = json.load(file)
            except json.JSONDecodeError as ex:
                logger.info(f"Ошибка декодирования JSON {ex}, файл поврежден или пуст")
                return []  # Ошибка декодирования JSON, файл поврежден или пуст
            if isinstance(fin_operation, list):
                return fin_operation  # Возвращаем список словарей
            else:
                logger.warning("Файл содержит не список")
                return []  # Файл содержит не список
    except Exception as ex:
        logger.error(f"Ошибка {ex}")
        return []  # Обработка любых других ошибок чтения файла


print(fin_trans())  # Пример корректного ввода
