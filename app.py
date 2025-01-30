from flask import Flask, render_template, request
from database import get_db_connection  # Подключаем функцию для работы с базой данных

app = Flask(__name__)  # Объект приложения должен быть инициализирован до использования маршрутов


@app.route('/')
def home():
    return render_template('index.html', title="Главная страница")


@app.route('/contacts')
def contacts():
    return render_template('contact.html', title="Контакты")


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        query = request.form['query']
        category = request.form['category']

        # Имитация долгого запроса (например, работа с парсером или API)
        time.sleep(2)  # Можно заменить на реальную обработку данных

        return render_template('results.html', query=query, category=category)

    return render_template('form.html', title="Форма для ввода данных")


@app.route('/results', methods=['GET', 'POST'])
def results():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM vacancies')
    vacancies = cursor.fetchall()

    conn.close()

    return render_template('results.html', vacancies=vacancies)


if __name__ == "__main__":
    app.run(debug=True)
