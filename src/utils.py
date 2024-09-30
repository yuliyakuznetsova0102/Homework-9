import json
import logging
from json import JSONDecodeError
from typing import Any
from venv import logger

from src.external_api import currency_conversion

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(massage)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info(f"Получение данных из файла {path}")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                logger.error(f'Ошибка при чтении json-файла из файла "{path}"')
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        logger.error(f'Ошибка:файл "{path}" не найден')
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(trans)
        logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount
