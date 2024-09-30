import logging
from venv import logger

utils_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(massage)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирует номер карты"""
    logger.info("Создаю маску номера карты")
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Маска номера карты создана")
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        logger.error("Неправильный номер карты")
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Функция маскирует банковский счет"""
    logger.info("Создаю маску номера счета")
    if acc_number.isdigit() and len(acc_number) == 20:
        logger.info("Маска номера счета создана")
        return f"{"*" * 2}{acc_number[-4:]}"
    else:
        logger.error("Неправильный номер счета")
        return None
