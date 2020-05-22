sec = int(input())
h = sec // 3600 % 24
m = sec // 60 % 60
s = sec % 60
print(f"{h}:{m:02}:{s:02}")
