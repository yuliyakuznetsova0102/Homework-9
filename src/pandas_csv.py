import csv

import pandas as pd


def get_data_from_csv(path: str) -> list[dict]:
    """Функция получения данных из CSV-файла."""
    with open(path) as file:
        transaction_list = []
        py_file = csv.DictReader(file, delimiter=";")
        for row in py_file:
            transaction_list.append(row)
    return transaction_list


def get_data_from_excel(path: str) -> list[dict]:
    """Функция получения данных из файла Excel."""
    py_from_xlsx = pd.read_excel(path)
    py_dict = py_from_xlsx.to_dict(orient="records")
    return py_dict
