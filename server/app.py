#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return f'{parameter}'  # Display the string in the web browser with HTML tags

@app.route('/count/<int:num>')
def count(num):
    numbers = ''
    for i in range(0, num):
        numbers += str(i) + '\n'
    return f'{numbers}'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
