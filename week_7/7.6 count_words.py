words_set = set()

with open("input.txt", "r") as f:
    for line in f:
        for word in line.strip().split():
            words_set.add(word)

print(len(words_set))
