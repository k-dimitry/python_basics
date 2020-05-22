n = int(input())
buttons = [int(i) for i in input().split()]
k = int(input())
pushes = [int(i) for i in input().split()]

for i in pushes:
    buttons[i - 1] -= 1

for button in buttons:
    if button <= -1:
        print("YES")
    else:
        print("NO")
