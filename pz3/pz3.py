import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def get_currency_rates_last_week(currency_code='USD'):
    """
    Отримує курс вказаної валюти за останні 7 днів.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    dates = []
    rates = []

    print(f"Завантаження даних для {currency_code}...")


    current_date = start_date
    while current_date <= end_date:

        date_str_api = current_date.strftime('%Y%m%d')

        date_str_display = current_date.strftime('%d.%m')

        url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date={date_str_api}&json'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Перевірка на помилки HTTP
            data = response.json()

            if data:
                rate = data[0]['rate']
                dates.append(date_str_display)
                rates.append(rate)
                print(f"Дата: {date_str_display}, Курс: {rate}")
            else:
                print(f"Дані за {date_str_display} відсутні")

        except requests.exceptions.RequestException as e:
            print(f"Помилка при запиті: {e}")

        current_date += timedelta(days=1)

    return dates, rates


def plot_currency_rates(dates, rates, currency_code='USD'):

    if not dates or not rates:
        print("Немає даних для побудови графіка.")
        return

    plt.figure(figsize=(10, 6))  # Розмір вікна
    plt.plot(dates, rates, marker='o', linestyle='-', color='b', label=f'Курс {currency_code}')


    plt.title(f'Динаміка курсу {currency_code} за останній тиждень', fontsize=16)
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Курс (UAH)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()


    for i, txt in enumerate(rates):
        plt.annotate(f"{txt}", (dates[i], rates[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.show()


if __name__ == "__main__":

    dates_list, rates_list = get_currency_rates_last_week('USD')
    plot_currency_rates(dates_list, rates_list, 'USD')