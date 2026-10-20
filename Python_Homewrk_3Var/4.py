def rotate_right(a):
    if len(a) == 0:
     return []

    result = []

    for j in range(len(a[0])):
        row = []
        for i in range(len(a) - 1, -1, -1):
            row.append(a[i][j])
        result.append(row)

    return result







def rotate_left(a):
    if len(a) == 0:
      return []

    result = []

    for j in range(len(a[0]) - 1, -1, -1):
        row = []
        for i in range(len(a)):
            row.append(a[i][j])
        result.append(row)

    return result

for a in [
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2], [3, 4], [5, 6]],
    [[1, 2, 3]]
]:
    print("Исходная:", a)
    print("Вправо:", rotate_right(a))
    print("Влево:", rotate_left(a))