a, b, n = (int(input()) for _ in range(3))
price_cents = a * 100 + b
total_price = price_cents * n
print(total_price // 100, total_price % 100)
