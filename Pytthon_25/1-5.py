#1
lin = 0
words = 0
symbols = 0
max_len = 0

with open("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        lin += 1
        words += len(line.split())
        symbols += len(line)

        if len(line.rstrip("\r\n")) > max_len:
            max_len = len(line.rstrip("\r\n"))

print("Строк:", lin)
print("Слов:", words)
print("Символов:", symbols)
print("Самая длинная строка:", max_len)


#2
numbers = []

with open("numbers.txt", "r") as f:
    for line in f:
        try:
            numbers.append(int(line))
        except ValueError:
            print("Неверное число:", line.strip())

with open("result.txt", "w") as f:
    if len(numbers) > 0:
        f.write(f"Минимум: {min(numbers)}\n")
        f.write(f"Максимум: {max(numbers)}\n")
        f.write(f"Среднее: {sum(numbers) / len(numbers)}\n")
    else:
        f.write("Нет чисел")
        



#3
import csv

students = []

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        row["score"] = int(row["score"])
        students.append(row)

total = 0
best = students[0]
groups = {}

for student in students:
    total += student["score"]

    if student["score"] > best["score"]:
        best = student

    group = student["group"]

    if group not in groups:
        groups[group] = []

    groups[group].append(student["score"])

print("Средний балл:", total / len(students))
print("Лучший студент:", best["name"])

for group in groups:
    scores = groups[group]
    print(group, sum(scores) / len(scores))
    
    
    
#4
import csv

with open("products.csv", "r") as f:
    reader = csv.DictReader(f)

    with open("expensive.csv", "w", newline="") as result:
       writer = csv.DictWriter(result,name_up=["name", "category", "price"])
        
       writer.writeheader()

       for row in reader:
            if int(row["price"]) > 100:
                writer.writerow(row)
             
             
             
#5
import json

with open("students.json", encoding="utf-8") as file:
    students = json.load(file)

best_student = None

for student in students:
    student["passed"] = student["score"] >= 60

    if best_student is None or student["score"] > best_student["score"]:
        best_student = student

if best_student is not None:
    print("Лучший студент:", best_student["name"])
    print("Балл:", best_student["score"])
else:
    print("Список студентов пуст")

with open("students_result.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)