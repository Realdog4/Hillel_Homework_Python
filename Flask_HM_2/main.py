<<<<<<< Updated upstream
from flask import Flask, send_file, jsonify, request
from faker import Faker
# import requests
=======
from flask import Flask
from faker import Faker
import string
import random
>>>>>>> Stashed changes

app = Flask(__name__)
fake = Faker()

@app.route('/')
def openPage():
    return "Hello!"

@app.errorhandler(404)
def page_not_found(error):
    return "Помилка, введіть коректну адресу!", 404



<<<<<<< Updated upstream
=======
@app.route('/generate_password')
def generate_password():
    password_length = random.randint(10, 20)
    password_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    return f"New password: {password}"

>>>>>>> Stashed changes

@app.route('/mean/')
def get_mean():
    with open('hw.csv', 'r') as f:
        lines = f.readlines()[1:]
        heights = []
        weights = []
        for line in lines:
            parts = line.strip().split(',')
            weight = float(parts[1])
            weights.append(weight)
            height = float(parts[2])
            heights.append(height)

        mean_weight = round(sum(weights) / len(weights), 2)
        mean_height = round(sum(heights) / len(heights), 2)

<<<<<<< Updated upstream
        return f"Середній зріст: {mean_height} см, Середня вага: {mean_weight} кг"

=======
        return f"Average high: {mean_height} sm, Average weight: {mean_weight} kg"
>>>>>>> Stashed changes



if __name__ == '__main__':
    app.run()