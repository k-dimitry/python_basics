n = int(input())
d = {}

for _ in range(n):
    wrd1, wrd2 = input().split()
    d[wrd1] = wrd2
    d[wrd2] = wrd1

print(d[input()])
