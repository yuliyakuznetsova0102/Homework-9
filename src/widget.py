from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция получает строки и маскирует счет или карту"""
    new_number = ""
    if len(number.split()[-1]) == 16:
        new_number == get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number == get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает на вход строку с датой и возвращает строку с датой
    в формате 'ДД.ММ.ГГГГ'"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])
