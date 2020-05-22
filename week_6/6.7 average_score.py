d = {}
with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        line = line.strip()
        class_num, score = int(line.split()[2]), int(line.split()[3])
        if class_num not in d:
            d[class_num] = []
        d[class_num].append(score)

for class_num in sorted(d):
    print(sum(d[class_num]) / len(d[class_num]), end=" ")
