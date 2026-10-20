#6
from pathlib import Path

folder = Path(input("Каталог: "))

files = 0
directories = 0
total_size = 0
python_files = []

if not folder.is_dir():
    print("Каталог не найден")
else:
    for path in folder.rglob("*"):
        if path.is_file():
            files += 1
            total_size += path.stat().st_size

            if path.suffix == ".py":
                python_files.append(path)

        elif path.is_dir():
            directories += 1

    print("Файлов:", files)
    print("Подкаталогов:", directories)
    print("Общий размер:", total_size, "байт")
    print("Python-файлы:")

    for path in python_files:
        print(path)
        
        
        
#7
from pathlib import Path

folder = Path(input("Каталог: "))
extension = input("Расширение: ").strip()

if not extension.startswith("."):
    extension = "." + extension

try:
    if not folder.is_dir():
        print("Каталог не существует")
    else:
        found = False

        for path in folder.rglob("*"):
            if path.is_file() and path.suffix.lower() == extension.lower():
                print(path, "—", path.stat().st_size, "байт")
                found = True

        if not found:
            print("Файлы не найдены")

except OSError as error:
    print("Ошибка доступа к каталогу или файлу:", error)


#8
def read_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Файл не найден")

    except PermissionError:
        print("Нет прав доступа к файлу")

    except IsADirectoryError:
        print("Указан каталог вместо файла")

    except UnicodeError:
        print("Не удалось прочитать текст в кодировке UTF-8")

    except OSError as error:
        print("Другая ошибка операционной системы:", error)

    return None


text = read_file("text.txt")

if text is not None:
    print(text)


#9
def parse_number(value):
    return float(value)


text = input("Введите число: ")

try:
    number = parse_number(text)
    print("Получено число:", number)
except ValueError:
    print("Ошибка: введено не число")




#10
class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError()

    if amount > balance:
        raise InsufficientFundsError()

    return balance - amount



try:
    balance = withdraw(1000, 1500)
    print("Остаток:", balance)

except InvalidAmountError as e:
    print(e)

except InsufficientFundsError as e:
    print(e)