num1, num2 = int(input()), int(input())

for num in range(num1, num2 + 1):
    if str(num) == str(num)[::-1]:
        print(num)
