d = {}

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            d[word] = d.get(word, 0) + 1

print(sorted(d, key=lambda k: (-d[k], k))[0])
