max9, max10, max11 = -1, -1, -1
count9, count10, count11 = 1, 1, 1

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip().split()
        class_n, score = int(line[2]), int(line[3])
        if class_n == 9:
            if score > max9:
                max9 = score
                count9 = 1
            elif score == max9:
                count9 += 1
        elif class_n == 10:
            if score > max10:
                max10 = score
                count10 = 1
            elif score == max10:
                count10 += 1
        elif class_n == 11:
            if score > max11:
                max11 = score
                count11 = 1
            elif score == max11:
                count11 += 1

print(count9, count10, count11)
