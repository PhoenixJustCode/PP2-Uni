import psycopg2
import csv

# Database config
DB_NAME = "phonebook_db"
DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100),
                    phone VARCHAR(20) UNIQUE NOT NULL
                );
            """)
            conn.commit()
            print("Таблица создана.")


def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_user(%s, %s)", (name, phone))
                conn.commit()
                print("Контакт добавлен или обновлён.")
    except Exception as e:
        print("Ошибка:", e)


def insert_from_csv(csv_file):
    names, phones = [], []
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    names.append(row[0])
                    phones.append(row[1])

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
                conn.commit()
                print("Импорт завершён.")
    except Exception as e:
        print("Ошибка:", e)


def update_data():
    phone = input("Введите номер телефона для обновления: ")
    new_name = input("Новое имя (или пропустите): ")
    new_phone = input("Новый номер телефона (или пропустите): ")

    query_parts = []
    values = []

    if new_name:
        query_parts.append("first_name = %s")
        values.append(new_name)
    if new_phone:
        query_parts.append("phone = %s")
        values.append(new_phone)

    if not query_parts:
        print("Нет данных для обновления.")
        return

    values.append(phone)

    query = f"UPDATE phonebook SET {', '.join(query_parts)} WHERE phone = %s"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                if cur.rowcount:
                    print("Обновление выполнено.")
                else:
                    print("Контакт не найден.")
                conn.commit()
    except Exception as e:
        print("Ошибка:", e)


def search_by_pattern():
    pattern = input("Введите шаблон (часть имени или номера): ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Ошибка:", e)


def get_paginated():
    try:
        limit = int(input("Сколько записей показать? "))
        offset = int(input("С какого смещения начать? "))

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Ошибка:", e)


def delete_data():
    val = input("Введите имя или номер для удаления: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s)", (val,))
                conn.commit()
                print("Удаление выполнено.")
    except Exception as e:
        print("Ошибка:", e)


def main_menu():
    create_table()

    while True:
        print("\nМеню:")
        print("1. Добавить контакт (ручной ввод)")
        print("2. Импорт из CSV")
        print("3. Обновить контакт")
        print("4. Поиск по шаблону")
        print("5. Показать с пагинацией")
        print("6. Удалить контакт")
        print("0. Выход")

        choice = input("Выбор: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            csv_path = input("Путь к CSV: ")
            insert_from_csv(csv_path)
        elif choice == "3":
            update_data()
        elif choice == "4":
            search_by_pattern()
        elif choice == "5":
            get_paginated()
        elif choice == "6":
            delete_data()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main_menu()
