percent, rub, cop = (int(input()) for _ in range(3))
total_cop = cop + rub * 100
total_cop += total_cop * percent / 100
print(int(total_cop // 100), int(total_cop % 100))
