with open("input.txt", "r", encoding="utf8") as f, \
     open("output.txt", "w", encoding="utf8") as w:
    students = []
    for line in f:
        line = line.strip().split()
        line.pop(2)
        students.append(line)
        students.sort(key=lambda x: x[0])
    for student in students:
        w.write(" ".join(student) + "\n")
