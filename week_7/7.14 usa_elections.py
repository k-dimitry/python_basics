d = {}

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        line = line.strip().split()
        name, votes = line[0], int(line[1])
        d[name] = d.get(name, 0) + votes

for name in sorted(d):
    print(name, d.get(name))
