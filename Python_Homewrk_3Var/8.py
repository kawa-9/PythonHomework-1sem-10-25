import random
from functools import wraps


def retry(attempts):
    if type(attempts) is not int or attempts < 1:
        raise ValueError("Количество попыток должно быть целым и положительным")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Ошибка в попытке", attempt + 1)

                    if attempt == attempts - 1:
                        raise

        return wrapper

    return decorator


@retry(3)
def load_data():
    """Пример загрузки данных со случайной ошибкой."""
    if random.random() < 0.7:
        raise ValueError("Не удалось загрузить данные")

    return "Данные загружены"


try:
    print(load_data())
except ValueError as error:
    print("Все попытки закончились:", error)