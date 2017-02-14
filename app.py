from flask import Flask
app = Flask(__name__)
# Создаем экзэмпляр приложения


@app.route('/') # Ассоциация между адресом url и функцией
def index():
    return '<h1>Hello, world!</h1>'

@app.route('/user/<name>') # Включим переменный компонент name
def user(name):
    return '<h1>Hello, %s!' % name

if __name__ == '__main__':
    app.run(debug=True)