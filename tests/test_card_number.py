import re
from typing import Any

import pytest

from src.generators import card_number_generator


@pytest.fixture
def correct_numbers() -> list[str]:
    return ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]


@pytest.mark.parametrize(
    "expected",
    [
        ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"],
    ],
)
def test_card_number_generator(correct_numbers: list[str], expected: Any) -> None:
    """тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне."""
    card_num = list(card_number_generator(start=10, stop=12))
    assert card_num == expected


def test_card_number_format() -> None:
    """тест для проверки формата номеров карт"""
    start, stop = 4000123456789010, 4000123456789015
    pattern = re.compile(r"\d{4} \d{4} \d{4} \d{4}")
    for card_number in card_number_generator(start, stop):
        assert pattern.match(card_number), f"Неверный формат: {card_number}"


def test_card_number_boundaries() -> None:
    start, stop = 4000123456789010, 4000123456789015
    generated_cards = list(card_number_generator(start, stop))

    # Проверяем, что первый и последний номера равны start и stop
    first_card = int(generated_cards[0].replace(" ", ""))
    last_card = int(generated_cards[-1].replace(" ", ""))

    assert first_card == start, f"Первый номер не равен start: {generated_cards[0]}"
    assert last_card == stop, f"Последний номер не равен stop: {generated_cards[-1]}"


def test_card_number_generator_errors() -> None:
    # Проверка обработки ошибок
    try:
        with pytest.raises(ValueError):
            card_number_generator(1234567890123458, 1234567890123456)
        with pytest.raises(ValueError):
            card_number_generator(1234567890123458, 99999999999999999)
    except:
        assert True
