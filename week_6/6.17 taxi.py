lst1 = sorted([int(i) for i in input().split()])
lst2 = sorted([int(i) for i in input().split()], reverse=True)

print(sum(a * b for a, b in zip(lst1, lst2)))
