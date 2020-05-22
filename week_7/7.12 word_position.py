d = {}
with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            print(d.get(word, 0), end=" ")
            d[word] = d.get(word, 0) + 1
