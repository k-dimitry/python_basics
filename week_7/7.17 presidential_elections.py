d = {}
total_votes = 0

with open("input.txt", "r", encoding="utf8") as f, \
        open("output.txt", "w", encoding="utf8") as w:
    for line in f:
        name = line.strip()
        d[name] = d.get(name, 0) + 1
        total_votes += 1

    winners = sorted(d, key=lambda k: -d[k])
    if d.get(winners[0]) > total_votes / 2:
        w.write(winners[0])
    else:
        w.write(winners[0] + "\n" + winners[1])
