import csv
from pathlib import Path

filepath_csv = Path("..", "data", "transactions.csv")


def read_financial_operations(csv_file_path):
    """
    Считывает финансовые операции из CSV-файла.
    :param csv_file_path: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    transactions = []
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                transactions.append(row)

        return transactions
    except FileNotFoundError:
        # Если файл не найден, возбуждаем исключение FileNotFoundError
        raise FileNotFoundError(f"No such file or directory")
    except Exception as e:
        # Обработка других возможных ошибок
        print(f"Произошла ошибка при чтении файла: {e}")
        raise  # Перевыбрасываем исключение для дальнейшей обработки вызывающим кодом


# Пример использования
transactions = read_financial_operations(filepath_csv)
print(transactions)
