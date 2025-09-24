import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def get_rub_amount(transaction):
    """
    Возвращает сумму транзакции в рублях (float).
    Если валюта USD или EUR, конвертирует через API.
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
    to = "RUB"

    if currency == "RUB":
        return float(amount)
    elif currency in ("USD", "EUR"):
        try:
            headers = {"apikey": os.getenv("API_KEY_currency")}
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"
            response = requests.get(url, headers=headers)
            data = response.json()
            rate = data["result"]
            time.sleep(5)
            return float(rate)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None  # Возвращаем None в случае ошибки API
        except (KeyError, TypeError) as e:
            print(f"Ошибка обработки ответа API: {e}")
            return None  # Возвращаем None в случае ошибки формата ответа
    else:
        return None  # Валюта не поддерживается


# transactions = fin_trans(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))
# for transaction in transactions:
#     amount_rub = get_rub_amount(transaction)
#     print(f"Транзакция: {amount_rub} RUB")
