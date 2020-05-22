percent, rub, cop, years = (int(input()) for _ in range(4))
total_cop = cop + rub * 100

for _ in range(years):
    total_cop += total_cop * percent / 100
    rub = int(total_cop // 100)
    cop = int(total_cop % 100)
    total_cop = cop + rub * 100

print(int(total_cop // 100), int(total_cop % 100))
