a, b, c, a1, b1, c1 = (int(input()) for _ in range(6))
s1 = (a // a1) * (b // b1) * (c // c1)
s2 = (a // b1) * (b // a1) * (c // c1)
s3 = (a // c1) * (b // a1) * (c // b1)
s4 = (a // a1) * (b // c1) * (c // b1)
s5 = (a // b1) * (b // c1) * (c // a1)
s6 = (a // c1) * (b // b1) * (c // a1)
print(max(s1, s2, s3, s4, s5, s6))
