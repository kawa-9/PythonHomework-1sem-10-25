import numpy as np


def find_anomalies(numbers, k):
    if k < 0:
        raise ValueError("k не может быть отрицательным")

    if not numbers:
        return []

    average = sum(numbers) / len(numbers)

    total = 0
    for number in numbers:
        total += (number - average) ** 2

    deviation = (total / len(numbers)) ** 0.5

    result = []
    for number in numbers:
        if abs(number - average) > k * deviation:
            result.append(number)

    return result


def find_anomalies_numpy(numbers, k):
    if k < 0:
        raise ValueError("k не может быть отрицательным")

    if not numbers:
        return []

    values = np.array(numbers, dtype=float)
    average = np.mean(values)
    deviation = np.std(values)

    return values[np.abs(values - average) > k * deviation].tolist()


for numbers in ([10, 11, 12, 10, 11, 100], [5, 5, 5], []):
    result1 = find_anomalies(numbers, 2)
    result2 = find_anomalies_numpy(numbers, 2)

    print("Обычный вариант:", result1)
    print("Вариант с numpy:", result2)
    print("Результаты совпадают:", result1 == result2)