total_votes = 0
parties_lst = []
parties_dict = {}

with open("input.txt", "r", encoding="utf8") as f:
    first_line = f.readline()
    for line in f:
        line = line.strip()
        if "VOTES" in line:
            break
        parties_dict[line] = 0
        parties_lst.append(line)
    for line in f:
        line = line.strip()
        parties_dict[line] += 1
        total_votes += 1

seven_percent = total_votes * 7 / 100
for party in parties_lst:
    if parties_dict[party] >= seven_percent:
        print(party)
