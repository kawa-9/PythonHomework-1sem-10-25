#16
import re

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_users = set()

pattern = (
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
    r"(INFO|WARNING|ERROR)\b"
)

with open("server.log", encoding="utf-8") as file:
    for line in file:
        match = re.match(pattern, line)

        if match:
            level = match.group(1)
            counts[level] += 1

            if level == "ERROR":
                user = re.search(r"\bUser ([0-9]+)\b", line)

                if user:
                    error_users.add(user.group(1))

for level, count in counts.items():
    print(f"{level}: {count}")

print("Пользователи с ошибками:", sorted(error_users))




#17
total = 0
count = 0
minimum = None
maximum = None

with open("numbers.txt", encoding="utf-8") as file:
    for line in file:
        try:
            number = int(line)
        except ValueError:
            continue

        total += number
        count += 1

        if minimum is None or number < minimum:
            minimum = number

        if maximum is None or number > maximum:
            maximum = number

print("Сумма:", total)
print("Количество:", count)

if count > 0:
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print("Среднее:", total / count)
else:
    print("В файле нет чисел")
    
    
    
    
#18
import re
import json
import logging

logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8"
)


def analyze_log(filename):
    pattern = re.compile(
        r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
        r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) "
        r"(?P<method>[A-Z]+) "
        r"(?P<url>\S+) "
        r"(?P<code>[1-5][0-9]{2})\s*$"
    )

    methods = {}
    urls = {}
    errors = 0
    count = 0

    logging.info("Начало обработки файла %s", filename)

    try:
        with open(filename, encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                match = pattern.match(line)

                if match is None:
                    logging.warning("Пропущена строка %s", line_number)
                    continue

                ip = match.group("ip")
                method = match.group("method")
                url = match.group("url")
                code = int(match.group("code"))

                if any(int(part) > 255 for part in ip.split(".")):
                    logging.warning("Неверный IP в строке %s", line_number)
                    continue

                count += 1
                methods[method] = methods.get(method, 0) + 1
                urls[url] = urls.get(url, 0) + 1

                if 400 <= code <= 499:
                    errors += 1

    except (OSError, UnicodeError) as error:
        logging.error("Ошибка чтения: %s", error)
        print("Не удалось прочитать файл:", error)
        return

    popular_url = None
    if urls:
        popular_url = max(urls, key=urls.get)

    result = {
        "total_requests": count,
        "methods": methods,
        "errors_4xx": errors,
        "most_popular_url": popular_url
    }

    try:
        with open("statistics.json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    except OSError as error:
        logging.error("Ошибка сохранения: %s", error)
        print("Не удалось сохранить статистику:", error)
        return

    logging.info("Обработка завершена. Запросов: %s", count)
    print(result)


analyze_log("access.log")



#19
import re

text = """
Телефоны:
+7 999 123-45-67
8 999 123-45-67
+7 (999) 123-45-67
8 (999) 123-45-67
"""

pattern = (
    r"(?<!\w)(?:\+7|8) "
    r"(?:[0-9]{3}|\([0-9]{3}\)) "
    r"[0-9]{3}-[0-9]{2}-[0-9]{2}(?!\w)"
)

phones = re.findall(pattern, text)

for phone in phones:
    print(phone)
    
    
    
    
    
#20
import re

text = """
Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026.
Следующая встреча запланирована на 1.11.2026.
"""

dates = re.findall(r"\b[0-9]{2}\.[0-9]{2}\.[0-9]{4}\b", text)

for value in dates:
    print(value)