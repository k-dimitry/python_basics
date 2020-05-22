lst = list(map(int, input().split()))
n = int(input())

for i, num in enumerate(lst):
    if n > num:
        print(i + 1)
        break
else:
    print(len(lst) + 1)
