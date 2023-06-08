import pandas as pd
from flask import Flask, request
from faker import Faker

app = Flask(__name__)
fake = Faker()

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



if __name__ == '__main__':
    app.run()
