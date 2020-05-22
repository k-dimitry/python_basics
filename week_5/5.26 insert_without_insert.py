lst = input().split()
k, c = map(int, input().split())

lst.append("*")
for i in range(len(lst) - 1, k - 1, -1):
    lst[i] = lst[i - 1]

lst[k] = c
print(*lst)
