import csv
import random
import math
from datetime import date, timedelta


def generate_sales(filename, count=5000):
    products = ["Book", "Pen", "Notebook", "Pencil"]
    start = date(2026, 1, 1)

    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "product", "quantity", "price"])

        for i in range(count):
            if i % 20 == 0:
                writer.writerow(["wrong date", "Book", "ошибка", -100])
                continue

            day = start + timedelta(days=random.randint(0, 364))
            product = random.choice(products)
            quantity = random.randint(1, 10)
            price = random.randint(50, 1000)

            writer.writerow([day, product, quantity, price])


def analyze_sales(filename):
    total = 0
    purchases = 0
    quantities = {}
    revenues = {}
    days = {}

    with open(filename, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                day = date.fromisoformat(row["date"]).isoformat()
                product = row["product"].strip()
                quantity = int(row["quantity"])
                price = float(row["price"])

                if not product or quantity <= 0 or price < 0:
                    continue
                if not math.isfinite(price):
                    continue

                cost = quantity * price
                if not math.isfinite(cost):
                    continue

            except (ValueError, TypeError, KeyError, AttributeError):
                continue

            total += cost
            purchases += 1

            quantities[product] = quantities.get(product, 0) + quantity
            revenues[product] = revenues.get(product, 0) + cost
            days[day] = days.get(day, 0) + cost

    if purchases == 0:
        print("В файле нет корректных продаж")
        return

    print("Общая сумма продаж:", round(total, 2))
    print("Самый продаваемый товар:", max(quantities, key=quantities.get))
    print("Товар с максимальной выручкой:", max(revenues, key=revenues.get))
    print("Средняя стоимость покупки:", round(total / purchases, 2))
    print("День с максимальной выручкой:", max(days, key=days.get))


generate_sales("sales.csv")
analyze_sales("sales.csv")