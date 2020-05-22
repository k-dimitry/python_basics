n, k = map(int, input().split())
lst = ["I"] * n

for _ in range(k):
    l, r = map(int, input().split())
    lst[l - 1: r] = ["."] * (r - l + 1)

print(*lst, sep="")
