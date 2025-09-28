from pathlib import Path

import pandas as pd

filepath_xlsx = Path("..", "data", "transactions_excel.xlsx")


def read_excel_file(excel_file_path):
    """
    Считывает финансовые операции из excel-файла.
    :param excel_file_path: Путь к excel-файлу
    :return: Список словарей с транзакциями
    """

    try:
        reader = pd.read_excel(excel_file_path)
        dict_list = reader.to_dict(orient="records")
        return dict_list

    except FileNotFoundError:
        # Если файл не найден, возбуждаем исключение FileNotFoundError
        raise FileNotFoundError("No such file or directory")
    except Exception as e:
        # Обработка других возможных ошибок
        print(f"Произошла ошибка при чтении файла: {e}")
        raise  # Перевыбрасываем исключение для дальнейшей обработки вызывающим кодом


print(read_excel_file(filepath_xlsx))
