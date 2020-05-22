parties_dict = {}

with open("input.txt", "r", encoding="utf8") as f:
    first_line = f.readline()
    for line in f:
        line = line.strip()
        if "VOTES" in line:
            break
        parties_dict[line] = 0
    for line in f:
        line = line.strip()
        parties_dict[line] += 1

for key, value in sorted(parties_dict.items(), key=lambda kv: (-kv[1], kv[0])):
    print(key)
