import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card() -> str :
    return "7000 79** **** 6361"

def test_get_mask_card_number(card: str) -> None:
    """Функция тестирует правильность маскирования номера карты."""
    assert get_mask_card_number("7000792289606361") == card





@pytest.fixture
def acc() -> str :
    return "**4305"

def test_get_mask_account(acc: str) -> None:
    assert get_mask_account("73654108430135874305") == acc
