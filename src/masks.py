import logging
import os

os.makedirs("logs", exist_ok=True)

# Настройка логирования
log_file_path = os.path.join("logs", "masks.log")
logger = logging.getLogger("masks.log")
logging.basicConfig(
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="w", encoding="utf-8"),
        logging.StreamHandler(),  # Дополнительно выводим логи в консоль
    ],
)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде
    числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX."""
    logger.debug("Запуск работы функции")
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        mask_number = f"{card_number_str[:4]} {card_number_str[4:6]} ** **** {card_number_str[12:]}"
        logger.info("Номер карты замаскирован")
        return mask_number
    logger.error("Некорректный ввод")
    return "Некорректный ввод"


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    logger.debug("Запуск работы функции")
    account_str = str(account)
    if len(account_str) >= 4:
        mask_account = f"**{account_str[-4:]}"
        logger.info("Номер счёта замаскирован")
        return mask_account
    logger.error("Некорректный ввод")
    return "Некорректный ввод"


# print(get_mask_card_number(1234123412341234))
# print(get_mask_account(98797298340))

print(get_mask_card_number(1234567812345678))  # Пример корректного ввода
print(get_mask_card_number(12345))  # Пример некорректного ввода
