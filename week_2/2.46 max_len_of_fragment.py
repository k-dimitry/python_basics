number = int(input())
i = 1
max_num = number
b = 1
c = 1
d = 1
e = 1
f = 1
while number != 0:
    number = int(input())
    if number == 0:
        break
    elif number > max_num:
        d = 1
        i += 1
        max_num = number
        if i > b:
            c = b
            b = i
    elif number < max_num:
        i = 1
        d += 1
        max_num = number
        if d > e:
            f = e
            e = d
    elif number == max_num:
        max_num = number
        d = 1
        i = 1
print(max(b, e))
