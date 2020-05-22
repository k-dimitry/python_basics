lst9 = []
lst10 = []
lst11 = []

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        line = line.strip().split()
        class_n, score = int(line[-2]), int(line[-1])
        if class_n == 9 and score not in lst9:
            lst9.append(score)
        elif class_n == 10 and score not in lst10:
            lst10.append(score)
        elif class_n == 11 and score not in lst11:
            lst11.append(score)

lst9.sort(reverse=True)
if len(lst9) >= 2:
    print(lst9[1], end=" ")
else:
    print(0, end=" ")
lst10.sort(reverse=True)
if len(lst10) >= 2:
    print(lst10[1], end=" ")
else:
    print(0, end=" ")
lst11.sort(reverse=True)
if len(lst11) >= 2:
    print(lst11[1], end=" ")
else:
    print(0, end=" ")
