def filter_by_state(list_dict: list[dict]) -> list[dict]:
    """Функция,возвращает новый список словарей, содержащий только те словари,
       у которых ключ 'state' соответствует указанном значению"""
    sorted_list = sorted(list_dict, key=lambda x: x["state"], reverse=True)
    return sorted_list


def sort_by_date(list_dict: list[dict]) -> list[dict]:
    """Функция, возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=True)
    return sorted_list
