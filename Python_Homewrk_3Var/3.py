def top_symbols(s):
    counts = {}

    for c in s.lower():
        if c != " ":
            if c not in counts:
                counts[c] = 0
            counts[c] += 1


print(top_symbols("Hello World"))
print(top_symbols("aabbccdde"))
print(top_symbols(""))