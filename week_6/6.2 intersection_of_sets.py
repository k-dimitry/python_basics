lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]

p1, p2 = 0, 0
result_lst = []

while p1 < len(lst1) and p2 < len(lst2):
    num1, num2 = lst1[p1], lst2[p2]
    if num1 == num2:
        result_lst.append(num1)
        p1 += 1
        p2 += 1
    elif num1 > num2:
        p2 += 1
    elif num2 > num1:
        p1 += 1

print(*result_lst)
