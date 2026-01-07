import os


def analyze_log_file(log_file_path):

    status_counts = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) >= 9:
                    status_code = parts[8]
                    if status_code.isdigit():
                        if status_code in status_counts:
                            status_counts[status_code] += 1
                        else:
                            status_counts[status_code] = 1

    except FileNotFoundError:
        print(f"Помилка: Файл '{log_file_path}' не знайдено.")
        return {}
    except IOError as e:
        print(f"Помилка вводу/виводу при читанні файлу: {e}")
        return {}
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return {}

    return status_counts



def create_dummy_log(filename):
    """Створює тестовий файл логів для перевірки."""
    content = """127.0.0.1 - - [10/Oct/2023:13:55:36 -0700] "GET /index.html HTTP/1.0" 200 2326
192.168.0.1 - - [10/Oct/2023:13:55:37 -0700] "GET /image.png HTTP/1.0" 200 4056
127.0.0.1 - - [10/Oct/2023:13:55:38 -0700] "POST /login HTTP/1.0" 404 123
10.0.0.5 - - [10/Oct/2023:13:55:39 -0700] "GET /admin HTTP/1.0" 403 500
127.0.0.1 - - [10/Oct/2023:13:55:40 -0700] "GET /data HTTP/1.0" 500 1024
192.168.0.1 - - [10/Oct/2023:13:55:41 -0700] "GET /style.css HTTP/1.0" 200 2326
127.0.0.1 - - [10/Oct/2023:13:55:42 -0700] "GET /favicon.ico HTTP/1.0" 404 200"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Створено тестовий файл: {filename}")


if __name__ == "__main__":
    log_name = "apache_logs.txt"
    create_dummy_log(log_name)

    print("\n--- Результат аналізу ---")
    results = analyze_log_file(log_name)

    for code, count in results.items():
        print(f"Код {code}: {count} разів")

    print("\n--- Тест помилки (відсутній файл) ---")
    analyze_log_file("non_existent_file.txt")