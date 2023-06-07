from flask import Flask, send_file, jsonify, request
from faker import Faker
# import requests

app = Flask(__name__)
fake = Faker()

@app.route('/')
def openPage():
    return "Hello!"

@app.errorhandler(404)
def page_not_found(error):
    return "Помилка, введіть коректну адресу!", 404




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

        return f"Середній зріст: {mean_height} см, Середня вага: {mean_weight} кг"




if __name__ == '__main__':
    app.run()