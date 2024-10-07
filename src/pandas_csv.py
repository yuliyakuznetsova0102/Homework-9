import csv

import pandas as pd


def get_data_from_csv(file: str) -> list[dict]:
    """Функция считывающая cvs файл и возвращающая список словарей"""
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)

    return result


def get_data_from_xlsx(file: str) -> list[dict]:
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    df = pd.read_excel(file)
    result = []
    rows_count = len(df)
    for i in range(0, rows_count):
        row_dict = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": str(df.at[i, "from"]),
            "to": str(df.at[i, "to"]),
        }
        result.append(row_dict)
    return result
