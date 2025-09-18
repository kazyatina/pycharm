import unittest
from unittest.mock import MagicMock, Mock, patch

import requests

from src.external_api import get_rub_amount


class TestGetRubAmount(unittest.TestCase):
    """Тесты для функции get_rub_amount."""

    @patch("requests.get")
    @patch("os.getenv", return_value="test_api_key")
    def test_usd_to_rub_conversion(self, mock_getenv, mock_get):
        """Проверяем конвертацию USD в RUB через API."""

        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 75.50}
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "1",
                "currency": {
                    "code": "USD"
                }
            }
        }
        result = get_rub_amount(transaction)
        self.assertEqual(result, 75.50)

        mock_get.assert_called_once()  # Проверяем, что API был вызван


    @patch("requests.get")  # Патчим requests.get в вашем модуле
    @patch("os.getenv")  # Патчим os.getenv для получения API_KEY
    def test_get_rub_amount_rub(self, mock_getenv, mock_get):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}

        # Вызов функции
        result = get_rub_amount(transaction)

        # Проверка результата
        self.assertEqual(result, 100.0)

    @patch("requests.get")
    @patch("os.getenv")
    def test_get_rub_amount_usd(self, mock_getenv, mock_get):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}

        mock_getenv.return_value = "dummy_api_key"  # Устанавливаем тестовый API_KEY
        mock_response = Mock()
        mock_response.json.return_value = {"result": 7500}  # Тестовый курс
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Вызов функции
        result = get_rub_amount(transaction)

        # Проверка результата
        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once()

    @patch("requests.get")
    @patch("os.getenv")
    def test_get_rub_amount_eur(self, mock_getenv, mock_get):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}

        mock_getenv.return_value = "dummy_api_key"
        mock_response = Mock()
        mock_response.json.return_value = {"result": 8500}  # Тестовый курс
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Вызов функции
        result = get_rub_amount(transaction)

        # Проверка результата
        self.assertEqual(result, 8500.0)
        mock_get.assert_called_once()

    @patch("requests.get")
    @patch("os.getenv")
    def test_get_rub_amount_api_error(self, mock_getenv, mock_get):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}

        mock_getenv.return_value = "dummy_api_key"
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        # Вызов функции
        result = get_rub_amount(transaction)

        # Проверка результата
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch("requests.get")
    @patch("os.getenv")
    def test_get_rub_amount_invalid_currency(self, mock_getenv, mock_get):
        """Проверяем, что для неподдерживаемой валюты возвращается None."""
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBP"}}}  # Неподдерживаемая валюта

        # Вызов функции
        result = get_rub_amount(transaction)

        # Проверка результата
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
