from flask import Flask
from faker import Faker
import string
import random
import pandas as pd

app = Flask(__name__)
fake = Faker()

@app.route('/')
def openPage():
    return "Hello!"

@app.errorhandler(404)
def page_not_found(error):
    return "Помилка, введіть коректну адресу!", 404


@app.route('/generate_password')
def generate_password():
    password_length = random.randint(10, 20)
    password_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(password_characters, k=password_length))

    return f"New password: {password}"


@app.route('/mean/')
def get_mean():
    data = pd.read_csv('hw.csv', delimiter=',\s+', engine='python')
    data['Height(Inches)'] = pd.to_numeric(data['Height(Inches)'], errors='coerce')
    data['Weight(Pounds)'] = pd.to_numeric(data['Weight(Pounds)'], errors='coerce')

    average_height = round(data['Height(Inches)'].mean(), 2)
    average_weight = round(data['Weight(Pounds)'].mean(), 2)

    return f"Average high: {average_height} sm, Average weight: {average_weight} kg"




if __name__ == '__main__':
    app.run()