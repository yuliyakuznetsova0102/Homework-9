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
