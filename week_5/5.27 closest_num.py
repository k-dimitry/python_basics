n = int(input())
lst = [int(i) for i in input().split()]
x = int(input())
num = lst[0]

for i in lst:
    if abs(x - i) < abs(x - num):
        num = i

print(num)
