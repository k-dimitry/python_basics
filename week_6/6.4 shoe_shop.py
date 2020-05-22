n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
counter = 0
index = 0

for i in range(len(lst)):
    if lst[i] >= n:
        counter += 1
        n = lst[i]
        index = i
        break

for i in lst[index + 1:]:
    if i - n >= 3:
        counter += 1
        n = i

print(counter)
