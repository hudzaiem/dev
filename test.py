import unittest
import pandas as pd
import numpy as np
from unittest.mock import patch
from main import main
from utilities.util import preproccess
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utilities')))

class TestMain(unittest.TestCase):

    @patch('main.bigquery.Client.insert_rows_json')
    def test_main(self, mock_insert_rows_json):
        mock_insert_rows_json.return_value = []

        main()

        self.assertTrue(mock_insert_rows_json.called)
        self.assertEqual(mock_insert_rows_json.call_args[0][0], 'price-forecasting-try.scraping_hargapangan.daily_scraping')
        self.assertIsInstance(mock_insert_rows_json.call_args[0][1], list)
        self.assertGreater(len(mock_insert_rows_json.call_args[0][1]), 0)

    def test_util(self):
        df = pd.DataFrame({
            'value': [1, np.nan, 3],
            'date': ['2022-01-01', '2022-01-02', '2022-01-03']
            })
        Expected_df = [
        {'value': 1.0, 'date': '2022-01-01 00:00:00'},
        {'value': 0.0, 'date': '2022-01-02 00:00:00'},
        {'value': 3.0, 'date': '2022-01-03 00:00:00'}
        ]
        self.assertEqual(preproccess(df),Expected_df)


if __name__ == '__main__':
    unittest.main()