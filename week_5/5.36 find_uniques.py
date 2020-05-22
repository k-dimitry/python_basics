lst = [int(i) for i in input().split()]
result_lst = []

for n in lst:
    if lst.count(n) == 1:
        result_lst.append(n)

print(*result_lst)
