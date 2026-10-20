#11
import re

user_ids = []
error_lines = []
error_users = set()

with open("logs.txt", encoding="utf-8") as file:
    for line in file:
        ids = re.findall(r"\bUser ([0-9]+)\b", line)
        user_ids.extend(ids)

        if re.match(r"ERROR\b", line):
            error_lines.append(line.rstrip())
            error_users.update(ids)

print("Все идентификаторы:", user_ids)

print("Строки с ERROR:")
for line in error_lines:
    print(line)

print("Пользователи с ошибками:", sorted(error_users))



#12
import re

text = """
Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

emails = re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    text
)

unique_emails = []

for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)

for email in unique_emails:
    print(email)





 #13
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, error_type, error, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Время: {elapsed:.6f} сек.")
        return False


with Timer():
    result = sum(range(1_000_000))

print(result)


#Через contextlib.contextmanager:


import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.perf_counter()

    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"Время: {elapsed:.6f} сек.")


with timer():
    result = sum(range(1_000_000))

print(result)




 #14
from contextlib import contextmanager


@contextmanager
def log_operation(filename, operation):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"START: {operation}\n")
        file.flush()

        try:
            yield
        except BaseException:
            file.write(f"ERROR: {operation}\n")
            raise
        else:
            file.write(f"END: {operation}\n")


with log_operation("operation.log", "Data processing"):
    print("Выполняется обработка данных")





 #15
from io import StringIO


def count_lines(stream):
    count = 0

    for line in stream:
        count += 1

    return count


with open("data.txt", encoding="utf-8") as file:
    print("Строк в файле:", count_lines(file))

with StringIO("first\nsecond\nthird") as stream:
    print("Строк в StringIO:", count_lines(stream))