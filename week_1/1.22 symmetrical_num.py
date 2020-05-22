num = int(input())
thousands = num // 1000
hundreds = num % 1000 // 100
tens = num % 100 // 10
ones = num % 10
x1 = thousands - ones
x2 = hundreds - tens
print(0 ** (x1 ** 2 + x2 ** 2))
