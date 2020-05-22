lst = [int(num) for num in input().split()]
flag = True

for i in range(len(lst) - 1):
    if lst[i] >= lst[i + 1]:
        flag = False
        break

print("YES" if flag else "NO")
