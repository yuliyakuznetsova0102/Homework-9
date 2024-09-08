import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card() -> str :
    return "7000 79** **** 6361"

def test_get_mask_card_number(card: str) -> None:
    """Функция тестирует правильность маскирования номера карты."""
    assert get_mask_card_number("7000792289606361") == card


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
def test_get_mask_card_number(num, expected) -> None:
    assert get_mask_card_number(num) == expected



@pytest.fixture
def acc() -> str :
    return "**4305"

def test_get_mask_account(acc: str) -> None:
    assert get_mask_account("73654108430135874305") == acc


@pytest.mark.parametrize(
    "acc, res",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
        ("89909221136652296582", "**6582"),
        ("59994142284263533658", "**3658"),
    ],
)
def test_get_mask_account(acc, res) -> None:
    assert get_mask_account(acc) == res