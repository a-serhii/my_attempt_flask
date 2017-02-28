from flask import Flask, request, make_response, redirect, render_template
from flask.ext.moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
# Создаем экзэмпляр приложения
app.config['SECRET_KEY'] = 'hard to guess string'
# Настраиваем ключ шифрования

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name, dude?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])  # Ассоциация между адресом url и функцией
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name )


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)