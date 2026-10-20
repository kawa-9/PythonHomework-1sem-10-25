def longest_s(a):
    if len(a) == 0:
        return 0

    best = 1
    count = 1
    number = a[0]

    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            count += 1
        else:
            count = 1

        if count > best:
            best = count
            number = a[i]

    return best, number

print(longest_s([1, 1, 1, 2, 2, 3, 3, 3, 3]))
print(longest_s([5, 5, 2, 2, 7]))
print(longest_s([]))
