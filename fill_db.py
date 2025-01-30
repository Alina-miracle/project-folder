from app import db, Category, Vacancy

def fill_database():
    # Добавление категорий
    it_category = Category(name="IT")
    marketing_category = Category(name="Marketing")

    db.session.add(it_category)
    db.session.add(marketing_category)
    db.session.commit()

    # Добавление вакансий
    vacancy1 = Vacancy(title="Software Engineer", description="Develop software applications.", salary=120000, category_id=it_category.id)
    vacancy2 = Vacancy(title="Marketing Manager", description="Lead marketing campaigns.", salary=80000, category_id=marketing_category.id)

    db.session.add(vacancy1)
    db.session.add(vacancy2)
    db.session.commit()

if __name__ == "__main__":
    fill_database()
