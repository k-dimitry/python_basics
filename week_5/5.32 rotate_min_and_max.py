lst = [int(n) for n in input().split()]

min_n, max_n = min(lst), max(lst)
min_i, max_i = lst.index(min_n), lst.index(max_n)
lst[min_i], lst[max_i] = lst[max_i], lst[min_i]

print(*lst)
