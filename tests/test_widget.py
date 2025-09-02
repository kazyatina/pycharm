import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card , expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83 ** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30 ** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> str:
    assert mask_account_card(account_card) == expected


@pytest.fixture
def get_date_status() -> list:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-02-10T01:25:17.671407", "10.02.2023"),
    ]


@pytest.mark.parametrize(
    "date, expected",
    [
        (num, expected)
        for num, expected in [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2023-02-10T01:25:17.671407", "10.02.2023"),
        ]
    ],
)
def test_get_date(date: str, expected: str) -> str:
    assert get_date(date) == expected
