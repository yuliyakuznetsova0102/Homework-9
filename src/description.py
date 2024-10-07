import re
from collections import Counter


def filter_by_request(transaction_list: list[dict], user_request: str) -> list[dict]:
    """Функция фильтрации транзакций по запросу пользователя."""

    target_list = []
    lower_user_request = user_request.lower()
    for transaction in transaction_list:
        if re.search(lower_user_request, transaction.get("description", ""), flags=re.IGNORECASE):
            target_list.append(transaction)
        else:
            continue
    print(target_list)
    return target_list


def count_transaction_categories(transactions: list[dict]) -> dict:
    """Функция подсчета транзакций по типу категории."""

    categories = []
    for transaction in transactions:
        categories.append(transaction["description"])
    counted = dict(Counter(categories))
    print(counted)
    return counted
