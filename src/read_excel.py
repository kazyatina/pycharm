from pathlib import Path

import pandas as pd

filepath_xlsx = Path("..", "data", "transactions_excel.xlsx")


def read_excel_file(excel_file_path):
    """
    Считывает финансовые операции из excel-файла.
    :param excel_file_path: Путь к excel-файлу
    :return: Список словарей с транзакциями
    """

    transactions = []
    try:
        with open(excel_file_path, mode="r", encoding="utf-8") as file_ex:
            reader = pd.read_excel(file_ex)
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


excel_data = pd.read_excel(filepath_xlsx)
print(excel_data.head())
