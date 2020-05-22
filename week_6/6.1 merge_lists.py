lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]

p1 = p2 = 0
result_lst = []

while p1 < len(lst1) and p2 < len(lst2):
    if lst1[p1] < lst2[p2]:
        result_lst.append(lst1[p1])
        p1 += 1
    elif lst1[p1] > lst2[p2]:
        result_lst.append(lst2[p2])
        p2 += 1
    else:
        result_lst.append(lst1[p1])
        p1 += 1

if p1 == len(lst1):
    result_lst += lst2[p2:]
else:
    result_lst += lst1[p1:]

print(*result_lst)
