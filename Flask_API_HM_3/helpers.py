
import pandas as pd
import requests
from http import HTTPStatus


def save_to_csv(student):
    df = pd.DataFrame(student, index=[0])
    df.to_csv('students.csv', mode='a', index=False, header=not df.empty)


def get_symbol(currency):
    url = 'https://bitpay.com/currencies'
    response = requests.get(url, {})
    if response.status_code == HTTPStatus.OK:
        data = response.json()
        for currency_data in data['data']:
            if currency_data['code'] == currency:
                symbol = currency_data['symbol']
                return symbol