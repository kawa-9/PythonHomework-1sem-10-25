from datetime import date


class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Количество должно быть целым и неотрицательным")

        self.name = name
        self.price = price
        self.quantity = quantity

    def final_price(self):
        return self.price


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def final_price(self):
        return round(self.price * 0.9, 2)


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty  # Гарантия в месяцах

    def final_price(self):
        return self.price


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = date.fromisoformat(expiration_date)

    def final_price(self):
        if self.expiration_date < date.today():
            raise ValueError("Срок годности продукта истёк")

        return round(self.price * 0.95, 2)


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def sell(self, name, quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Количество должно быть целым и положительным")

        product = self.find_product(name)

        if product is None:
            raise ValueError("Товар не найден")

        if quantity > product.quantity:
            raise ValueError("Недостаточно товара на складе")

        total = round(product.final_price() * quantity, 2)
        product.quantity -= quantity
        return total


def main():
    store = Store()

    store.add_product(Book("Python", 1000, 5, "Иван Иванов"))
    store.add_product(Electronic("Телефон", 30000, 3, 12))
    store.add_product(Food("Сок", 100, 10, "2030-12-31"))

    # Полиморфизм: один метод вызывается у разных типов товаров.
    for product in store.products:
        print(product.name, product.final_price())

    print("Стоимость покупки:", store.sell("Python", 2))
    print("Осталось книг:", store.find_product("Python").quantity)

    try:
        store.sell("Телефон", 100)
    except ValueError as error:
        print(error)


main()