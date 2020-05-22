lst = [int(i) for i in input().split()]
counter = 0
index = 1

for i in lst:
    for num in lst[index:]:
        if i == num:
            counter += 1
    index += 1

print(counter)
