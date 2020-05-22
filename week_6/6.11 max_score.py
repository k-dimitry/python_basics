d = {}
max9, max10, max11 = 0, 0, 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        class_n, score = (int(line.strip().split()[2]),
                          int(line.strip().split()[3]))
        if class_n == 9 and score > max9:
            max9 = score
        elif class_n == 10 and score > max10:
            max10 = score
        elif class_n == 11 and score > max11:
            max11 = score

print(max9, max10, max11)
