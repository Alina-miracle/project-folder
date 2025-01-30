from database import get_db_connection


def insert_test_data():
    test_data = [
        ('Junior Python Developer', 'We are looking for a Junior Python Developer...', 'Tech Corp', 'IT', 'Almaty'),
        ('Marketing Specialist', 'Join our marketing team...', 'Marketing Group', 'Marketing', 'Astana'),
        ('Senior Backend Developer', 'Looking for an experienced backend developer...', 'Dev Studio', 'IT', 'Almaty')
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO vacancies (title, description, company, category, location)
        VALUES (?, ?, ?, ?, ?)
    ''', test_data)

    conn.commit()
    conn.close()
    print("Тестовые данные успешно добавлены!")


if __name__ == "__main__":
    insert_test_data()
