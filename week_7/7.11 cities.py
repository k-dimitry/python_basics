n = int(input())

d = {}
for _ in range(n):
    enter = input().strip().split()
    country, cities = enter[0], enter[1:]
    for city in cities:
        d[city] = country

m = int(input())
for _ in range(m):
    print(d.get(input().strip()))
