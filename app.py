from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения
app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacancies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определение модели Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    vacancies = db.relationship('Vacancy', backref='category', lazy=True)

# Определение модели Vacancy
class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Vacancy {self.title}>"

# Создание базы данных
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vacancies')
def vacancies():
    all_vacancies = Vacancy.query.all()  # Получаем все вакансии из базы
    return render_template('vacancies.html', vacancies=all_vacancies)

if __name__ == "__main__":
    app.run(debug=True)
