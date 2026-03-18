from flask import Flask, render_template, request
import os

app = Flask(__name__)

projects = [
    {
        "title": "Игра на Python",
        "description": "Игра Крестики-нолики с графическим интерфейсом.",
        "image": "project1.png",
        "tech": ["Python, Pygame"]
    },
    {
        "title": "Игра на C++",
        "description": "Консольная игра 'РПГ-квест'. Научился работать с циклами.",
        "image": "project2.png",
        "tech": ["C++, Vector, Map"]
    },
    {
        "title": "Этот сайт-портфолио",
        "description": "Веб-приложение на Flask. Изучил основы backend-разработки, маршрутизацию и работу с шаблонами.",
        "image": "project3.png",
        "tech": ["Python", "Flask", "HTML/CSS"]
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    message_sent = False

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(name, email, message)  # можно убрать потом

        message_sent = True

    return render_template('contacts.html', message_sent=message_sent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))