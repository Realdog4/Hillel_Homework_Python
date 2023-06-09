import pandas as pd
from flask import Flask, request, Response
from faker import Faker
import requests
from http import HTTPStatus

app = Flask(__name__)
fake = Faker()


@app.route('/')
def openPage():
    return "Hello! Use the link to view information: /generate_students or /bitcoin_rate"

@app.errorhandler(404)
def page_not_found(error):
    return "Error, please enter the correct address!", 404


@app.route('/generate_students', methods=['GET'])
def generate_students():
    count = int(request.args.get('count', 1000))
    students = []

    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)

        student = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'birthday': birthday
        }

        students.append(student)
        save_to_csv(student)

    return '\n'.join([str(student) for student in students]), 200, {'Content-Type': 'text/plain'}

def save_to_csv(student):
    df = pd.DataFrame(student, index=[0])
    df.to_csv('students.csv', mode='a', index=False, header=not df.empty)



@app.route('/bitcoin_rate', methods=['GET'])
def get_bitcoin_value(currency='USD', count=1):
    url = 'https://bitpay.com/rates'
    response = requests.get(url, {})

    if response.status_code != HTTPStatus.OK:
        return Response(
            "ERROR: Something went wrong",
            status=response.status_code
        )

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        for currency_data in data['data']:
            if currency_data['code'] == currency:
                rate = currency_data['rate']
                symbol = get_symbol(currency)
                total = rate * count
                return f"The Bitcoin rate for {currency} is: {total} {symbol}"

def get_symbol(currency):
    url =  'https://bitpay.com/currencies'
    response = requests.get(url, {})
    if response.status_code == HTTPStatus.OK:
        data = response.json()
        for currency_data in data['data']:
            if currency_data['code'] == currency:
                symbol = currency_data['symbol']
                return symbol


if __name__ == '__main__':
    app.run()
