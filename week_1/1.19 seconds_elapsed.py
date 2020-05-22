h1, m1, s1 = (int(input()) for _ in range(3))
h2, m2, s2 = (int(input()) for _ in range(3))
print(h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1))
