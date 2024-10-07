import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_nums(card: str) -> None:
    """Функция тестирует правильность маскирования номера карты."""
    assert get_mask_card_number("7000792289606361") == card
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "num, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(num: str, expected: str) -> None:
    assert get_mask_card_number(num) == expected


def test_get_mask_account(acc: str) -> None:
    assert get_mask_account("73654108430135874305") == acc
    assert get_mask_account("70007962522289606361") == "**6361"
