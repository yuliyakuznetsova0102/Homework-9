import logging

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирует номер карты"""
    masks_logger.info("Создаю маску номера карты")
    if card_number.isdigit() and len(card_number) == 16:
        masks_logger.info("Маска номера карты создана")
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        masks_logger.error("Неправильный номер карты")
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Функция маскирует банковский счет"""
    masks_logger.info("Создаю маску номера счета")
    if acc_number.isdigit() and len(acc_number) == 20:
        masks_logger.info("Маска номера счета создана")
        return f"{"*" * 2}{acc_number[-4:]}"
    else:
        masks_logger.error("Неправильный номер счета")
        return None
