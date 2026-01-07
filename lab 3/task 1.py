import sqlite3
import hashlib

DB_FILE = "my_users.db"


def get_db_connection():
    return sqlite3.connect(DB_FILE)


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users
                   (
                       login
                       TEXT
                       PRIMARY
                       KEY,
                       password
                       TEXT
                       NOT
                       NULL,
                       full_name
                       TEXT
                       NOT
                       NULL
                   )
                   ''')
    conn.commit()
    conn.close()
    print(f"База даних '{DB_FILE}' та таблиця перевірені/створені.")


def add_user(login, password, full_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_pw = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)',
                       (login, hashed_pw, full_name))
        conn.commit()
        print(f"Користувача '{login}' успішно додано!")
    except sqlite3.IntegrityError:
        print(f"Помилка: Користувач з логіном '{login}' вже існує.")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        conn.close()


def update_password(login, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_pw = hash_password(new_password)
    cursor.execute('UPDATE users SET password = ? WHERE login = ?', (hashed_pw, login))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Пароль для '{login}' успішно оновлено.")
    else:
        print(f"Користувача з логіном '{login}' не знайдено.")
    conn.close()


def authenticate_user():
    login = input("Введіть логін для входу: ")
    password = input("Введіть пароль: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password, full_name FROM users WHERE login = ?', (login,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        stored_hash = user_data[0]
        full_name = user_data[1]
        if hash_password(password) == stored_hash:
            print(f"Успішний вхід! Вітаємо, {full_name}.")
            return True
        else:
            print("Невірний пароль.")
    else:
        print("Користувача з таким логіном не знайдено.")
    return False


def main():
    create_table()
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Зареєструвати нового користувача")
        print("2. Увійти в систему (Перевірка паролю)")
        print("3. Змінити пароль")
        print("4. Вихід")
        choice = input("Ваш вибір: ")

        if choice == '1':
            l = input("Введіть логін: ")
            p = input("Введіть пароль: ")
            n = input("Введіть повне ПІБ: ")
            add_user(l, p, n)
        elif choice == '2':
            authenticate_user()
        elif choice == '3':
            l = input("Введіть логін користувача: ")
            new_p = input("Введіть новий пароль: ")
            update_password(l, new_p)
        elif choice == '4':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()