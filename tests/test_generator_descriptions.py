from typing import Any

import pytest

from src.generators import transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод с карты на счет"},
    ]


@pytest.mark.parametrize(
    "expected",
    [
        ["Перевод организации", "Перевод с карты на счет"],
    ],
)
def test_transaction_descriptions(transactions: list[dict], expected: Any) -> None:
    """ Тест на корректный вывод"""
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected


@pytest.fixture
def empty_descriptions() -> list:
    return []


@pytest.mark.parametrize(
    "expected",
    [
        ["Перевод организации", "Перевод с карты на счет"],
    ],
)
def test_empty_descriptions(empty_descriptions: list, expected: Any) -> None:
    """ Тест на проверку пустого списка"""
    empty_list = list(transaction_descriptions(empty_descriptions))
    assert empty_list == ["Описания транзакций нет."]
