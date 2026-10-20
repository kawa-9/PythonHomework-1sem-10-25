def chess(n, m, first=0, second=1):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(first)
            else:
                row.append(second)
        matrix.append(row)

    return matrix

for row in chess(3, 5):
    print(*row)

print()
for row in chess(4, 3, "B", "W"):
    print(*row)

print()