from flask import Flask, render_template, request
import time  # Для имитации долгих запросов

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title="Главная страница")


@app.route('/contacts')
def contacts():
    return render_template('contact.html', title="Контакты")


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Получаем данные формы
        query = request.form['query']
        category = request.form['category']

        # Здесь имитируем поиск (например, подключение к API или парсеру)
        time.sleep(2)  # Имитация долгого запроса

        # Переходим на страницу результатов с переданными данными
        return render_template('results.html', query=query, category=category)

    return render_template('form.html', title="Форма для ввода данных")


if __name__ == "__main__":
    app.run(debug=True)
