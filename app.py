from flask import Flask, request, make_response
app = Flask(__name__)
# Создаем экзэмпляр приложения


@app.route('/') # Ассоциация между адресом url и функцией
def index():
    return '<h1>Hello, world!</h1>'


@app.route('/user/<name>') # Включим переменный компонент name
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/browser/')
def your_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


if __name__ == '__main__':
    app.run(debug=True)