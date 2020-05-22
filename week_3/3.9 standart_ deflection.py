lst = []
num = int(input())

while num != 0:
    lst.append(num)
    num = int(input())

s = sum(lst) / len(lst)
result = 0
for n in lst:
    result += (n - s) ** 2

result = (result / (len(lst) - 1)) ** 0.5
print(result)
