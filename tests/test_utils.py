import unittest
from unittest.mock import mock_open, patch

from src.utils import fin_trans


class TestFinTrans(unittest.TestCase):
    """Тесты для функции fin_trans."""

    @patch("os.path.exists")
    def test_file_not_exists(self, mock_exists):
        """Проверка, что функция возвращает пустой список, если файл не существует."""
        mock_exists.return_value = False
        self.assertEqual(fin_trans("fake_path.json"), [])

    @patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
    @patch("os.path.exists", return_value=True)
    def test_valid_json(self, mock_exists, mock_file):
        """Проверка, что функция возвращает список словарей при корректном JSON."""

        result = fin_trans("valid_path.json")
        self.assertEqual(result, [{"key": "value"}])

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    @patch("os.path.exists", return_value=True)
    def test_invalid_json_not_list(self, mock_exists, mock_file):
        """Проверка, что функция возвращает пустой список, если JSON - не список."""

        result = fin_trans("invalid_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=True)
    def test_file_error(self, mock_exists, mock_file):
        """Проверка, что функция возвращает пустой список при ошибке открытия файла."""
        mock_file.side_effect = Exception("File error")

        result = fin_trans("error_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    @patch("os.path.exists", return_value=True)
    def test_invalid_json_decode_error(self, mock_exists, mock_file):
        """Проверка, что функция возвращает пустой список при ошибке декодирования JSON."""

        result = fin_trans("decode_error_path.json")
        self.assertEqual(result, [])
