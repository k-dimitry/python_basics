n, m = map(int, input().split())
set_anya = set()
set_borya = set()

for _ in range(n):
    set_anya.add(int(input()))

for _ in range(m):
    set_borya.add(int(input()))

common = set_borya & set_anya
unique_anya = set_anya - set_borya
unique_borya = set_borya - set_anya

print(len(common))
print(*sorted(common))
print(len(unique_anya))
print(*sorted(unique_anya))
print(len(unique_borya))
print(*sorted(unique_borya))
