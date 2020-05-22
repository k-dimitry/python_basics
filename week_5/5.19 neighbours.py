lst = [int(n) for n in input().split()]

for i in range(len(lst) - 1):
    if (lst[i] > 0 and lst[i + 1] > 0 or
            lst[i] < 0 and lst[i + 1] < 0):
        print(lst[i], lst[i + 1])
        break
