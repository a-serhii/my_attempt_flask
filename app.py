from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
# Создаем экзэмпляр приложения
bootstrap = Bootstrap(app)


@app.route('/')  # Ассоциация между адресом url и функцией
def index():
    return render_template('index.html')


@app.route('/user/<name>')  # Включим переменный компонент name
def user(name):
    return render_template('user.html', name=name)


@app.route('/browser/')
def your_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/cookie/')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/habr/')
def habr():
    return redirect('https://habrahabr.ru/')


if __name__ == '__main__':
    app.run(debug=True)