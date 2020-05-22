max_volume, n = (int(i) for i in input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
total_archive = 0
counter = 0

for i in lst:
    total_archive += i
    if total_archive >= max_volume:
        break
    counter += 1

print(counter)
