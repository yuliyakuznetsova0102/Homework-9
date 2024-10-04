from unittest.mock import Mock, mock_open, patch

import pandas as pd

from src.pandas_csv import get_data_from_csv, get_data_from_xlsx


@patch("csv.reader")
def test_reader_file_transaction_csv(mock_reader):
    m = mock_open()
    mock_reader.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "Sol",
                "PEN",
                "Счет 58803664561298323391",
                "Счет 39745660563456619397",
                "Перевод организации",
            ],
        ]
    )

    with patch("builtins.open", m) as mocked_open:
        assert get_data_from_csv("transaction.csv") == [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            }
        ]

        mocked_open.assert_called_with("transaction.csv", "r", encoding="utf-8")
