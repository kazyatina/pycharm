import csv
import unittest
from unittest.mock import mock_open, patch


def read_financial_operations(csv_file_path):
    """
    Считывает финансовые операции из CSV-файла.

    :param csv_file_path: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    transactions = []
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


class TestReadFinancialOperations(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="date,amount,description\n2023-01-01,100.00,Income\n2023-01-02,50.00,Expense\n",
    )
    def test_read_financial_operations(self, mock_file):
        """Тестирование функции считывания финансовых операций с использованием mock."""
        expected_output = [
            {"date": "2023-01-01", "amount": "100.00", "description": "Income"},
            {"date": "2023-01-02", "amount": "50.00", "description": "Expense"},
        ]

        # Вызываем функцию, передавая путь к файлу (это будет имитация)
        result = read_financial_operations("mocked_file.csv")

        # Проверяем, что функция вернула ожидаемый результат
        self.assertEqual(result, expected_output)

        # Проверяем, что open() был вызван с правильным путём
        mock_file.assert_called_once_with("mocked_file.csv", mode="r", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
