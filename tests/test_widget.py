import pytest

from src.widget import get_new_data, mask_account_card


@pytest.mark.parametrize(
    "number, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number: str, mask: str) -> None:
    assert mask_account_card(number) == mask


def test_get_new_data() -> None:
    assert get_new_data("2018-07-11T02:26:18.671407") == "11.07.2018"
