# Гражданская оборона
n = input()
villages = []
for idx, num in enumerate([int(i) for i in input().split()]):
    villages.append([num, idx + 1])
m = input()
shelters = []
for idx, num in enumerate([int(i) for i in input().split()]):
    shelters.append([num, idx + 1])
villages.sort()
shelters.sort()

length = len(shelters)
index = 0

for vil in villages:
    for i in range(index, length):
        if vil[0] == shelters[i][0]:
            vil.append(shelters[i][1])
            break
        elif (abs(vil[0] - shelters[i][0]) <
              abs(vil[0] - shelters[(i + 1) % length][0])):
            vil.append(shelters[i][1])
            break
        elif (abs(vil[0] - shelters[i][0]) >
              abs(vil[0] - shelters[(i + 1) % length][0])):
            index += 1
        elif (abs(vil[0] - shelters[i][0]) ==
              abs(vil[0] - shelters[(i + 1) % length][0])):
            vil.append(shelters[i][1])

villages.sort(key=lambda k: k[1])
print(*list(vil[2] for vil in villages))
