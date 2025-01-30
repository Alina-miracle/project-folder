import sqlite3

def get_db_connection():
    conn = sqlite3.connect('vacancies.db', check_same_thread=False)  # Важно: check_same_thread=False
    conn.row_factory = sqlite3.Row  # Для удобства работы с результатами
    return conn