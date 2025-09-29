import unittest
from unittest.mock import patch

import pandas as pd


# Предположим, что у нас есть функция read_excel_data, которую мы хотим протестировать
def read_excel_data(file_path):
    """Считывает данные из Excel файла и возвращает DataFrame."""
    df = pd.read_excel(file_path)
    return df


class TestReadExcelData(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_excel_file_success(self, mock_read_excel):
        """Тест, проверяющий успешное чтение данных из Excel."""
        # Подготавливаем ожидаемые данные
        expected_data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        mock_read_excel.return_value = expected_data

        # Вызываем функцию, которую тестируем
        actual_data = read_excel_data("dummy_path.xlsx")

        # Проверяем, что pandas.read_excel была вызвана с правильным аргументом
        mock_read_excel.assert_called_once_with("dummy_path.xlsx")
        # Сравниваем возвращенные данные с ожидаемыми
        pd.testing.assert_frame_equal(actual_data, expected_data)

    @patch("pandas.read_excel")
    def test_read_excel_data_file_not_found(self, mock_read_excel):
        """Тест, проверяющий обработку ошибки, если файл не найден."""
        mock_read_excel.side_effect = FileNotFoundError("No such file or directory")

        with self.assertRaises(FileNotFoundError):
            read_excel_data("nonexistent_file.xlsx")

        mock_read_excel.assert_called_once_with("nonexistent_file.xlsx")


if __name__ == "__main__":
    unittest.main()
