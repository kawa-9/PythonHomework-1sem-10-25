#21
import re


def is_valid_login(login):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,15}", login) is not None


logins = [
    "user_123",
    "admin",
    "123user",
    "ab",
    "user-name",
    "very_long_username"
]

for login in logins:
    print(login, "→", is_valid_login(login))
    
    
    
#22

import re

text = """
Полезные сайты: https://python.org, http://example.com/page,
https://example.com/docs/index.html и ftp://files.example.com/data.
"""

urls = re.findall(r"https?://[^\s,<>\"']+", text)

for url in urls:
    print(url.rstrip(".;!?)"))
    
    
    
#23
import re

text1 = "Это   строка    с     большим    количеством   пробелов."
text2 = "   Текст   с   пробелами   "

print(re.sub(r" {2,}", " ", text1).strip())
print(re.sub(r" {2,}", " ", text2).strip())


#24
import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

result = []

for product in products:
    if re.fullmatch(r"PRD-[0-9]{5}", product):
        result.append(product)

print(result)




#25
import re

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

pattern = (
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARNING|ERROR) "
    r"User (?P<user_id>[0-9]+) "
    r"(?P<message>.+)"
)

for line in logs:
    match = re.fullmatch(pattern, line)

    if match:
        print(match.groupdict())