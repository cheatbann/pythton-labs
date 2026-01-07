def filter_ips(input_file_path, output_file_path, allowed_ips):

    allowed_ips_set = set(allowed_ips)

    ip_counts = {}

    try:

        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue


                parts = line.split()

                if len(parts) > 0:
                    ip_address = parts[0]


                    if ip_address in allowed_ips_set:
                        if ip_address in ip_counts:
                            ip_counts[ip_address] += 1
                        else:
                            ip_counts[ip_address] = 1

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            if not ip_counts:
                print("Увага: Жодної дозволеної IP-адреси не знайдено у логах.")

            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

        print(f"Обробку завершено. Результати записано у '{output_file_path}'")

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{input_file_path}' не знайдено.")
    except IOError as e:
        print(f"Помилка вводу/виводу (читання або запис файлу): {e}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")

def create_test_log(filename):
    """Створює тестовий лог-файл."""
    content = """192.168.1.1 - - [10/Oct/2023] "GET /index.html" 200
10.0.0.1 - - [10/Oct/2023] "POST /login" 200
192.168.1.1 - - [10/Oct/2023] "GET /style.css" 200
172.16.0.5 - - [10/Oct/2023] "GET /admin" 403
10.0.0.1 - - [10/Oct/2023] "GET /about" 200
192.168.1.50 - - [10/Oct/2023] "GET /image.png" 200"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    input_log = "server_log.txt"
    output_log = "filtered_ips.txt"
    create_test_log(input_log)
    my_allowed_ips = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]

    print("--- Початок роботи ---")
    filter_ips(input_log, output_log, my_allowed_ips)
    print("\n--- Вміст вихідного файлу ---")
    try:
        with open(output_log, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Вихідний файл не створено через помилку.")