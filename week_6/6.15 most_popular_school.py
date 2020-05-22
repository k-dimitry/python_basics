schools = [0] * 99
results = []
finalists = []

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        school_n = int(line.strip().split()[-2])
        schools[school_n - 1] += 1

for i in range(len(schools)):
    if schools[i] != 0:
        results.append([schools[i], i + 1])

results = sorted(results, reverse=True)
max_s = results[0][0]

for res in results:
    if res[0] == max_s:
        finalists.append(res[1])
    else:
        break

print(*sorted(finalists))
