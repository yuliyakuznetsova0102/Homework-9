import json
import re
from collections import Counter
from src.decorators import log


def bank_operations(list_json: str, search: str) -> list[dict]:
    """Функция, которая возвращает данные с помощью поиска"""
    with open(list_json, encoding='utf-8') as f:
        data = json.load(f)
        operations_ = []
        for i in data:
            if i.get('state'):
                operations_.append(i)
        return [trans for trans in operations_ if re.search(search, trans['state'])]


def operations_in_json(transactions: str, category: str) -> dict:
    """Функция, которая принимает список с банковскими операциями и возвращает,
    их по ключу и значению"""
    with open(transactions, encoding='utf-8') as f:
        sentence = json.load(f)
        operations = []
        for i in sentence:
            if i.get('description'):
                operations.append(i)
        result = [category for trans in operations if re.findall(category, trans['description'])]

        count_operations = dict(Counter(result))
        return count_operations


@log("logs/work_func.txt")
def find_transactions(operations: list[dict], enter: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    return [operation for operation in operations if re.search(enter, operation.get("description", ""))]


@log("logs/work_func.txt")
def filtering_operations(operations: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    filt = [operation["description"] for operation in operations if operation.get("description", "") in categories]

    return dict(Counter(filt))


if __name__ == '__main__':
    bank_operations(r'../data\operations.json', 'CANCELED')
    bank_operations(r'../data\operations.json', 'PENDING')
    bank_operations(r'../data\operations.json', 'EXECUTED')
    operations_in_json(r'../data\operations.json', "Открытие вклада")
    operations_in_json(r'../data\operations.json', 'Перевод организации')
    operations_in_json(r'../data\operations.json', 'Перевод с карты на карту')
    operations_in_json(r'../data\operations.json', "Перевод с карты на счет")
    operations_in_json(r'../data\operations.json', "Перевод со счета на счет")