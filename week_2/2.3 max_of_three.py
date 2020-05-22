a, b, c = (int(input()) for _ in range(3))
if a < b > c:
    print(b)
elif a < c > b:
    print(c)
elif b < a > c:
    print(a)
elif a > b or a > c:
    print(a)
elif b > a or b > c:
    print(b)
else:
    print(c)
