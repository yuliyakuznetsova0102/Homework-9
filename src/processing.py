from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция,возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанном значению"""
    return [d for d in list_of_dict if d.get("state") == state]
