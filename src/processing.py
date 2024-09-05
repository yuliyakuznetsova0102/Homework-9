from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция,возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанном значению"""
    return [d for d in list_of_dict if d.get("state") == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Функция, возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list