from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция получает строки и маскирует счет или карту"""
    if len(number.split()[-1]) == 16:
        result = f"{number[:-16]} {get_mask_card_number(number.split()[-1])}"
        return result
    elif len(number.split()[-1]) == 20:
        result = f"{number[:-20]} {get_mask_account(number.split()[-1])}"
        return result


def get_new_data(old_data: str) -> str:
    """Функция принимает на вход строку с датой и возвращает строку с датой
    в формате 'ДД.ММ.ГГГГ'"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])