import hashlib
import os


def generate_file_hashes(*file_paths):

    hashes_dict = {}

    for file_path in file_paths:
        try:
            sha256_hash = hashlib.sha256()

            with open(file_path, "rb") as f:

                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

            hashes_dict[file_path] = sha256_hash.hexdigest()

        except FileNotFoundError:
            print(f"Помилка: Файл '{file_path}' не знайдено.")
        except IOError as e:
            print(f"Помилка вводу/виводу при читанні '{file_path}': {e}")
        except Exception as e:
            print(f"Невідома помилка з файлом '{file_path}': {e}")

    return hashes_dict

def create_dummy_files():
    """Створює тимчасові файли для тесту."""
    files = {
        "test_file_1.txt": "Hello, World!",
        "test_file_2.txt": "Python is awesome."
    }
    for name, content in files.items():
        with open(name, "w", encoding="utf-8") as f:
            f.write(content)
    return list(files.keys())


if __name__ == "__main__":

    created_files = create_dummy_files()
    files_to_check = created_files + ["ghost_file.txt"]

    print("--- Початок обчислення хешів ---")
    result = generate_file_hashes(*files_to_check)

    print("\n--- Результати ---")
    for path, hash_val in result.items():
        print(f"Файл: {path}")
        print(f"SHA-256: {hash_val}")
        print("-" * 20)
    for f in created_files:
        if os.path.exists(f):
            os.remove(f)