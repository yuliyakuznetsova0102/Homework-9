import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
HEADERS = os.getenv("PASSWORD")


def currency_conversion(transaction: Any) -> Any:
    """Функция конвертации"""
    amout = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amout)
    else:
        response = requests.get(
            url=f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amout}",
            headers=HEADERS,
        )
        result = response.json()
        return float(result["result"])
