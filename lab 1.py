def main():
    # Початковий склад
    inventory = {
        "яблука": 10,
        "банани": 3,
        "молоко": 8,
        "хліб": 4,
        "цукор": 15
    }

    def update_inventory(product, quantity):
        if product in inventory:
            inventory[product] += quantity
            # Якщо кількість стала 0 або менше, можна видаляти товар
            if inventory[product] <= 0:
                print(f"Попередження: товар '{product}' закінчився або пішов у мінус!")
        else:
            inventory[product] = quantity
        print(f"Склад оновлено: {product} -> {inventory[product]}")

    while True:
        print("\n--- МЕНЮ СКЛАДУ ---")
        print("1. Оновити кількість товару (додати/видалити)")
        print("2. Показати весь склад")
        print("3. Знайти продукти, яких мало (< 5)")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Введіть назву продукту: ").strip().lower()
            try:
                qty = int(input("Введіть кількість (додатне - додати, від'ємне - забрати): "))
                update_inventory(name, qty)
            except ValueError:
                print("Помилка: введіть ціле число!")

        elif choice == "2":
            print("\nПоточний стан складу:")
            for item, count in inventory.items():
                print(f"{item}: {count}")

        elif choice == "3":
            low_stock = [item for item, count in inventory.items() if count < 5]
            print(f"\nТовари, яких мало (< 5): {low_stock}")

        elif choice == "4":
            print("Роботу завершено.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()