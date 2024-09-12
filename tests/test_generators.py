from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[str]) -> Any:
    assert next(filter_by_currency(transactions, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_eu(transactions: list) -> Any:
    with pytest.raises(SystemExit, match="В транзакции нет такого кода") as exc_info:
        assert next(filter_by_currency(transactions, "EU")) == exc_info


def test_filter_by_currency_empty() -> Any:
    with pytest.raises(SystemExit, match="Нет транзакции") as exc_info:
        gen = filter_by_currency([], "")
        assert next(gen) == exc_info


def test_transaction_descriptions(transactions: list) -> Any:
    assert next(transaction_descriptions(transactions)) == "Перевод организации"


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (2, "Перевод со счета на счет"),
        (3, "Перевод с карты на карту"),
        (4, "Перевод организации"),
    ],
)
def test_transaction_descriptions_1(index: int, expected: str, transactions: list) -> Any:
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_transaction_descriptions_empty() -> Any:
    with pytest.raises(SystemExit, match="Нет транзакции") as exc_info:
        assert next(transaction_descriptions([])) == exc_info


def test_card_number_generator() -> Any:
    assert next(card_number_generator(38, 39)) == "0000 0000 0000 0038"


def test_card_number_generator_start() -> Any:
    assert next(card_number_generator(0, 1)) == "0000 0000 0000 0000"


def test_card_number_generator_stop() -> Any:
    assert next(card_number_generator(9999999999999999, 9999999999999999)) == "9999 9999 9999 9999"
