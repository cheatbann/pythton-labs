def main():

    # Для прикладу
    sales_log = [
        {"продукт": "ноутбук", "кількість": 2, "ціна": 20000},
        {"продукт": "мишка", "кількість": 10, "ціна": 150},
        {"продукт": "ноутбук", "кількість": 1, "ціна": 21000},
        {"продукт": "клавіатура", "кількість": 5, "ціна": 800},
    ]

    def calculate_revenue_by_product(sales_list):

        revenue_report = {}

        for sale in sales_list:
            product = sale["продукт"]
            income = sale["кількість"] * sale["ціна"]


            if product in revenue_report:
                revenue_report[product] += income
            else:
                revenue_report[product] = income

        return revenue_report

    while True:
        print("\n--- СТАТИСТИКА ПРОДАЖІВ ---")
        print("1. Додати новий продаж")
        print("2. Показати історію всіх продажів")
        print("3. Показати загальний дохід по товарах")
        print("4. Товари з доходом > 1000 (Топ продажів)")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            try:
                name = input("Назва продукту: ").strip().lower()
                qty = int(input("Кількість: "))
                price = float(input("Ціна за одиницю: "))
                new_sale = {"продукт": name, "кількість": qty, "ціна": price}
                sales_log.append(new_sale)
                print("Продаж успішно додано!")
            except ValueError:
                print("Помилка: введіть коректні числа для кількості та ціни!")

        elif choice == "2":
            print("\nІсторія продажів:")
            for i, sale in enumerate(sales_log, 1):
                print(f"{i}. {sale['продукт']}: {sale['кількість']} шт. по {sale['ціна']} грн")

        elif choice == "3":

            revenue_dict = calculate_revenue_by_product(sales_log)
            print("\nЗагальний дохід по кожному продукту:")
            for prod, total in revenue_dict.items():
                print(f"{prod.capitalize()}: {total} грн")

        elif choice == "4":
            revenue_dict = calculate_revenue_by_product(sales_log)
            high_revenue_products = [prod for prod, total in revenue_dict.items() if total > 1000]

            print("\nТовари з доходом більше 1000:")
            print(high_revenue_products)

        elif choice == "5":
            break

        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()