from database import get_db_connection


def get_vacancies():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM vacancies')
    vacancies = cursor.fetchall()

    for vacancy in vacancies:
        print(
            f"ID: {vacancy['id']}, Title: {vacancy['title']}, Company: {vacancy['company']}, Location: {vacancy['location']}")

    conn.close()


if __name__ == "__main__":
    get_vacancies()
