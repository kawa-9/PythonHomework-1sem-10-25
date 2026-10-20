def find_similar(strings):
    best_pair = None
    min_difference = None

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            first = strings[i]
            second = strings[j]

            if len(first) != len(second):
                continue

            difference = 0
            for position in range(len(first)):
                if first[position] != second[position]:
                    difference += 1

            if min_difference is None or difference < min_difference:
                min_difference = difference
                best_pair = (first, second, difference)

    return best_pair


print(find_similar(["abcdef", "abcxef", "xxxxxx", "cat"]))


print(find_similar(["a", "bb", "ccc"]))  
print(find_similar([]))              
print(find_similar(["cat", "cat"]))     