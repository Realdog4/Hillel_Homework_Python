from flask import Flask, Response, jsonify
from faker import Faker
import requests
from http import HTTPStatus
from webargs import fields
from webargs.flaskparser import use_kwargs
from helpers import save_to_csv, get_symbol

app = Flask(__name__)
fake = Faker()


@app.route('/')
def openPage():
    return "Hello! Use the link to view information: /generate_students?count=10 or /bitcoin_rate"

@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ["Invalid request."])

    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    else:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
        )


@app.route('/generate_students', methods=['GET'])
@use_kwargs({'count': fields.Int(required=True, validate=lambda val: 0 < val <= 1000)}, location="query")
def generate_students(count):
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



@app.route('/bitcoin_rate', methods=['GET'])
@use_kwargs({'currency': str, 'count': int}, location="query")
def get_bitcoin_value(currency='USD', count=1):

    url = 'https://bitpay.com/rates'
    response = requests.get(url, {})

    if response.status_code != HTTPStatus.OK:
        return Response(
            "ERROR: Something went wrong",
            status=response.status_code
        )

    data = response.json()
    for currency_data in data['data']:
        if currency_data['code'] == currency:
            rate = currency_data['rate']
    symbol = get_symbol(currency)
    total = rate * count
    return f"The Bitcoin rate for {currency} is: {total} {symbol}"



if __name__ == '__main__':
    app.run(port=5001, debug=True)
